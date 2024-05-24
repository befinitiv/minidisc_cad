# Minidisc

This repository contains the CAD files (PCB & mechanics) for the 8cm "minidisc" player project.

The PCB is designed using Kicad 8, the mechanics is designed using build123d.

## Buld123d environment installation

1. Install direnv
2. Go into the mech/ subfolder, so that the Python environment specified in .envrc file is loaded
3. Install packages: `pip install -r requirements.txt`
4. Start GUI: `jupyter lab`

# BOM
* Display: https://www.reichelt.de/grafik-oled-0-84-zoll-96x16-dot-weiss-ziff-ea-w096016-xblw-p364744.html?&nbc=1
* Bluray drive: https://www.reichelt.de/verbatim-externer-slimline-blu-ray-brenner-verbatim-43889-p264365.html?search=bluray
* Battery: https://www.reichelt.de/mp3-player-akku-fuer-apple-ipod-li-po-1043-mah-akku-30933-p224503.html?&trstct=pos_0&nbc=1
* All other parts are within the Kicad PCB BOM
