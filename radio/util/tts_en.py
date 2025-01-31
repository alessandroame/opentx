# -*- coding: utf-8 -*-

# English language sounds configuration

import json
from tts_common import filename


systemSounds = []
sounds = []

for i in range(100):
    systemSounds.append((str(i), filename(i)))
for i in range(9):
    systemSounds.append((str(100 * (i + 1)), filename(100 + i)))
for i, s in enumerate(["thousand", "and", "minus", "point"]):
    systemSounds.append((s, filename(109 + i)))
for i, (s, f) in enumerate([("volt", "volt0"), ("volts", "volt1"),
                            ("amp", "amp0"), ("amps", "amp1"),
                            ("milliamp", "mamp0"), ("milliamps", "mamp1"),
                            ("knot", "knot0"), ("knots", "knot1"),
                            ("meter per second", "mps0"), ("meters per second", "mps1"),
                            ("foot per second", "fps0"), ("feet per second", "fps1"),
                            ("kilometer per hour", "kph0"), ("kilometers per hour", "kph1"),
                            ("mile per hour", "mph0"), ("miles per hour", "mph1"),
                            ("meter", "meter0"), ("meters", "meter1"),
                            ("foot", "foot0"), ("feet", "foot1"),
                            ("degree celsius", "celsius0"), ("degrees celsius", "celsius1"),
                            ("degree fahrenheit", "fahr0"), ("degrees fahrenheit", "fahr1"),
                            ("percent", "percent0"), ("percent", "percent1"),
                            ("milliamp-hour", "mamph0"), ("milliamp-hours", "mamph1"),
                            ("watt", "watt0"), ("watts", "watt1"),
                            ("milli-watt", "mwatt0"), ("milli-watts", "mwatt1"),
                            ("D B", "db0"),("D B", "db1"),
                            ("r p m", "rpm0"),("r p m", "rpm1"),
                            ("g", "g0"),("g", "g1"),
                            ("degree", "degree0"), ("degrees", "degree1"),
                            ("radian", "rad0"), ("radians", "rad1"),
                            ("milliliter", "ml0"), ("milliliters", "ml1"),
                            ("fluid ounce", "founce0"), ("fluid ounces", "founce1"),
                            ("milliliter per minute", "mlpm0"), ("milliliters per minute", "mlpm1"),
                            ("hertz", "hertz0"), ("hertz", "hertz1"),
                            ("milisecond", "ms0"), ("miliseconds", "ms1"),
                            ("microsecond", "us0"), ("microseconds", "us1"),
                            ("kilometer", "km0"), ("kilometers", "km1"),
                            ("hour", "hour0"), ("hours", "hour1"),
                            ("minute", "minute0"), ("minutes", "minute1"),
                            ("second", "second0"), ("seconds", "second1"),
                            ]):
    systemSounds.append((s, filename(f)))
for i, s in enumerate(["point zero", "point one", "point two", "point three",
                       "point four", "point five", "point six",
                       "point seven", "point eight", "point nine"]):
    systemSounds.append((s, filename(167 + i)))
for s, f in [("trim center", "midtrim"),
             ("maximum trim reached", "maxtrim"),
             ("minimum trim reached", "mintrim"),
             ("timer 1 elapsed", "timovr1"),
             ("timer 2 elapsed", "timovr2"),
             ("timer 3 elapsed", "timovr3"),
             ("transmitter battery low", "lowbatt"),
             ("inactivity alarm", "inactiv"),
             ("throttle warning", "thralert"),
             ("switch warning", "swalert"),
             ("bad eeprom", "eebad"),
             ("Welcome to open tea ex!", "hello"),
             ("RF signal, low", "rssi_org"),
             ("RF signal, critical", "rssi_red"),
             ("radio antenna defective", "swr_red"),
             ("telemetry lost", "telemko"),
             ("telemetry recovered", "telemok"),
             ("trainer signal lost", "trainko"),
             ("trainer signal recovered", "trainok"),
             ("sensor lost", "sensorko"),
             ("servo overload", "servoko"),
             ("power overload", "rxko"),
             ("receiver still connected", "modelpwr"),
             ("aileron trim", "aileron_trim"),
             ("elevator trim", "elevator_trim"),
             ("throttle trim", "throttle_trim"),
             ("rudder trim", "rudder_trim"),
             ("main page", "main_page"),
             ("category enabled", "category_enabled"),
             ("category disabled", "category_disabled"),
             ]:
    systemSounds.append((s, filename(f)))
for i, (s, f) in enumerate([("armed", "armed"),
                            ("disarmed", "disarm"),
                            ("throttle  cut", "thrcut"),
                            ("throttle  active", "thract"),
                            ("gear!, up!", "gearup"),
                            ("gear!, down!", "geardn"),
                            ("flaps!, up!", "flapup"),
                            ("flaps!, down!", "flapdn"),
                            ("spoiler!, up!", "splrup"),
                            ("spoiler!, down!", "splrdn"),
                            ("trainer!, on!", "trnon"),
                            ("trainer!, off!", "trnoff"),
                            ("engine!, off!", "engoff"),
                            ("too. high!", "tohigh"),
                            ("too. low!", "tolow"),
                            ("low. battery!", "lowbat"),
                            ("crow!, on!", "crowon"),
                            ("crow!, off!", "crowof"),
                            ("rf. signal!, low!", "siglow"),
                            ("rf. signal!, critical!", "sigcrt"),
                            ("LQ", "lq"),
                            ("RF mode", "rfmode"),
                            ("high. speed. mode!, active", "spdmod"),
                            ("thermal. mode!, on", "thmmod"),
                            ("normal. mode!, on", "nrmmod"),
                            ("landing. mode!, on", "lnding"),
                            ("acro. mode!, on", "acro"),
                            ("flight mode one", "fm-1"),
                            ("flight mode two", "fm-2"),
                            ("flight mode three", "fm-3"),
                            ("flight mode four", "fm-4"),
                            ("flight mode five", "fm-5"),
                            ("flight mode six", "fm-6"),
                            ("flight mode seven", "fm-7"),
                            ("flight mode eight", "fm-8"),
                            ("vario!, on", "vrion"),
                            ("vario!, off", "vrioff"),
                            ("flight mode power", "fm-pwr"),
                            ("flight mode land", "fm-lnd"),
                            ("flight mode float", "fm-flt"),
                            ("flight mode speed", "fm-spd"),
                            ("flight mode fast", "fm-fst"),
                            ("flight mode normal", "fm-nrm"),
                            ("flight mode cruise", "fm-crs"),
                            ("flight mode acro", "fm-acr"),
                            ("flight mode race", "fm-rce"),
                            ("flight mode launch", "fm-lch"),
                            ("flight mode ping", "fm-png"),
                            ("flight mode thermal", "fm-thm"),
                            ("flight mode thermal left", "fm-thl"),
                            ("flight mode thermal right", "fm-thr"),
                            ("flight mode stabilize", "fm-stb"),
                            ("flight mode horizon", "fm-hor"),
                            ("flight mode angle", "fm-ang"),
                            ("flight mode idle up 1", "fm-id1"),
                            ("flight mode idle up 2", "fm-id2"),
                            ("low rate", "ratlow"),
                            ("medium rate", "ratmed"),
                            ("high rate", "rathi"),
                            ]):
    sounds.append((s, filename(f)))

ss=[]
for s in systemSounds:
    ss.append({ "id":s[1],"speech":s[0]})

os=[]
for s in sounds:
    os.append({ "id":s[1],"speech":s[0]})
 
jsonContent=json.dumps({ "systemSounds":ss,"otherSounds":os},indent=4)
f=open("sounds.json","w")
f.write(jsonContent)
f.close()
