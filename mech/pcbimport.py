#Requires https://github.com/realthunder/kicad_parser

from kicad_parser import KicadPCB
import numpy

pcb = KicadPCB.load('../pcb/minidisc.kicad_pcb')
origin = numpy.array(pcb.setup.grid_origin)

#in PCB we have set a local origin and the Y axis is swapped compared to mechanics construction
def pcb_to_mech(pt):
    ret = pt-origin
    ret[1] = -ret[1]
    return ret


def get_mounting_holes():
	mounting_holes = []
	for c in pcb.gr_circle:
			center = numpy.array(c.center)
			end = numpy.array(c.end)
			radius = numpy.linalg.norm(center-end)
			if radius != 0.75:
					continue
			mounting_holes.append(pcb_to_mech(center))
	return mounting_holes


def get_switches():
	switches = []
	for c in pcb.footprint:
			reference = c.property[0][1]
			if not reference.startswith('"SW') or reference == '"SW3"' or reference == '"SW1"':
					continue
			switches.append(pcb_to_mech(c.at[0:2]))
	return switches

def get_component_location(ref):
	for c in pcb.footprint:
		if c.property[0][1] == '"%s"' % ref:
			return pcb_to_mech(c.at[0:2])
