# -*- coding: utf-8 -*-

import re
import os


# -------------------------------------------------------------------
# A MODIFIER A MODIFIER A MODIFIER A MODIFIER A MODIFIER A MODIFIER
IN_FILE = "./db_countries.lua"
OUT_FILE = "./out.txt"
ENC_DIR = '''D:\DCS World\MissionEditor\data\scripts\Enc'''
# -------------------------------------------------------------------


''' output will be be what's written in OUT_FILE '''
output = []

''' compiling regexes for later use '''
re_unit_line = re.compile('^.*cnt_unit.*\.(?P<raw_cat>.*)\..*"(?P<raw_name>.*)".*')
re_cmt_line = re.compile('^--.*')

''' ordered, indexed list of countries by commented line '''
l_cnt = ['-- RUSSIA','--UKRAINE','-- USA','-- TURKEY','-- GERMANY','-- CANADA','-- UK','-- FRANCE','-- SPAIN','-- THE NETHERLANDS', '-- BELGIUM',
       '-- NORWAY','-- DENMARK','-- GEORGIA','-- ISRAEL','-- INSURGENTS','-- ABKHAZIA','-- SOUTH OSSETIA','-- ITALY']

''' list of units as described in the game folders (simply takes the file names without extension '''
l_SAM = [x[:-4] for x in os.listdir(os.path.join(ENC_DIR, 'SAM'))]
l_HELO = [x[:-4] for x in os.listdir(os.path.join(ENC_DIR, 'Helicopter'))]
l_STATIC = [x[:-4] for x in os.listdir(os.path.join(ENC_DIR, 'Building'))]
l_PLANE = [x[:-4] for x in os.listdir(os.path.join(ENC_DIR, 'Plane'))]
l_SHIP = [x[:-4] for x in os.listdir(os.path.join(ENC_DIR, 'Ship'))]
l_TEC = [x[:-4] for x in os.listdir(os.path.join(ENC_DIR, 'Tech'))]
l_WEAP = [x[:-4] for x in os.listdir(os.path.join(ENC_DIR, 'Weapon'))]

''' dictionnaries for unit names translation '''
d_PLANES = {
            'Su-27': 'Su-27S',
            'Tu-95MS': 'Tu-95',
            'B-52H': 'B52',
            'E-3A': 'E-3',
            'E-2C': 'E-2D',
            'F/A-18C': 'FA-18C',
            'RQ-1A Predator': 'MQ-1',
            'S-3B Tanker': 'S-3B',
            'MiG-29G': 'MiG-29A',
            }

d_HELOS = {
           'Mi-24V': 'Mi-24',
           'Mi-28N': 'Mi-28'
           }

d_SAM = {
         '1L13 EWR': 'radar 1L13',
         '55G6 EWR': 'radar 55G6',
         'SA-11 Buk SR 9S18M1': '9S18M1 BUK SR',
         'SA-11 Buk LN 9A310M1': 'Buk-M1 9A310M1',
         'Kub 1S91 str': 'Kub-M1 1S91',
         'Kub 2P25 ln': 'Kub 2P25',
         'Osa 9A33 ln': 'Osa 9A33',
         'Strela-10M3': 'Strela-10 9K35M3',
         '2S6 Tunguska': 'Tunguska-M1',
         'ZSU-23-4 Shilka': 'Shilka ZSU-23-4M3',
         'SA-18 Igla-S manpad': 'Igla-S',
         'S-125': '5p73 s-125 ln',
         'ZU-23 Emplacement Closed': 'ZU-23 Emplacement',
         'Ural-375 ZU-23': 'ZU-23 Ural',
         '5p73 s-125 ln': 'snr s-125 tr',
         'snr s-125 tr': 'p-19 s-125 sr',
         'Stinger manpad': 'Stinger',
         'SA-18 Igla manpad': 'Igla-S',
         'Dog Ear radar': 'radar Sborka',
         'S-300PS 64H6E sr': 'S-300PS, 64N6E',
         'S-300PS 54K6 cp': 'S-300PS, 5N63S',
         'S-300PS 40B6MD sr': 'S-300PS, 5N66M',
         'S-300PS 5P85D ln': 'S-300PS, 5P85D',
         'S-300PS 5P85C ln': 'S-300PS, 5P85S',
         'Patriot cp': 'PATRIOT, ANMSQ-104',
         'Patriot ln': 'PATRIOT, M-901',
         'Patriot str': 'PATRIOT, ANMPQ-53',
         'Roland ADS': 'Roland-2',
         'Roland Radar': 'radar TUR',
         'Gepard': 'Gepard-1A2',
         'Vulcan': 'Vulcan M-163',
         'Stinger manpad dsr': 'Stinger',
         'ZU-23 Insurgent': 'ZU-23',
         'ZU-23 Closed Insurgent': 'ZU-23 Emplacement',
         'Ural-375 ZU-23 Insurgent': 'ZU-23 Ural',
         'Hawk sr': 'Improved Hawk, ANMPQ-50',
         'Hawk tr': 'Improved Hawk, ANMPQ-46',
         'Hawk ln': 'Improved Hawk, M192',
         'M1097 Avenger': 'M1097 Avenger PMS',
         'S-300PS 40B6M tr': 'S-300PS, 30N6',

         }

d_TEC = {
         'MLRS':'M270 MLRS',
         'Leopard1A3': 'Leopard-1A3',
         'M 818': 'M818',
         'ZIL-4331': 'ZIL-4334',
         'Ural ATsP-6': 'ATsP-6',
         'ZiL-131 APA-80': 'Zil-131 APA-80',
         'ZIL-131 KUNG': 'ZiL-131 KUNG',
         'Ural-4320 APA-5D': 'APA-5D',
         'SAU Msta': 'SAU 2S19 Msta',
         'SAU Akatsia': 'SAU Akatsia',
         'SAU 2-C9': 'SAO 2S9 Nona',
         'Grad-URAL': 'Grad',
         'T-80UD': 'T-80UD',
         'IKARUS Bus': 'IKARUS-280',
         'VAZ Car': 'VAZ-2109',
         'Trolley bus': 'ZIU-9',
         'KAMAZ Truck': 'KAMAZ-41101',
         'LAZ Bus': 'LAZ-695',
         'SAU Gvozdika': 'SAU 2S1 Gvozdika',
         'BTR_D': 'BTR-RD',
         'T-90': 'T-90A',
         'Hummer': 'M1025 HMMWV',
         'M1043 HMMWV Armament': 'M1043 HMMWV',
         'M-1 Abrams': 'M1A2',
         'M-2 Bradley': 'M2A2',
         'MCV-80': 'MCV-80 Warrior',
         }

''' list of units that should be ignored, they are not in the encyclopedia, or I could not find them '''
d_IGNORE = ['SA-18 Igla-S comm', 'Paratrooper RPG-16', 'Paratrooper AKS-74','Stinger comm', 'SA-11 Buk CC 9S470M1', 'Infantry AK', '2B11 mortar', 'M978 HEMTT Tanker', 'HEMTT TFFT',
            'Soldier AK', 'Soldier RPG', 'SA-18 Igla comm', 'Stinger comm dsr', 'M-60', 'AAV7', 'Patriot ECS', 'Patriot EPP', 'Patriot AMG', 'Challenger2', 'p-19 s-125 sr',
            'Soldier M4', 'Soldier M249', 'Boman', 'Predator GCS', 'Predator TrojanSpirit']

''' start the giz '''
with open(IN_FILE) as f:
    c = f.readlines()
    cur_cnt = None
    name = None
    cat = None
    for x in c:
        x = x.rstrip('\n')
        re_match = re.match(re_cmt_line, x)
        if re_match:
            if x in l_cnt:
                cur_cnt_id = l_cnt.index(x)
            else:
                pass
                #print 'Unknown country %s' % x
        re_match = re.match(re_unit_line, x)
        if re_match:
            raw_cat = re_match.group('raw_cat')
            raw_name = re_match.group('raw_name')
            if raw_cat in 'Planes':
                cat = 'Plane'
                if raw_name in l_PLANE:
                    name = raw_name
                else:
                    if raw_name in d_PLANES.keys():
                        name = d_PLANES[raw_name]
                    elif 'F-16' in raw_name:
                        name = 'F-16C'
                    elif 'Tornado' in raw_name:
                        name = 'Tornado'
                    elif 'Tu-95' in raw_name:
                        name = 'Tu-95'
                    else:
                        print 'unkown raw_name: %s' % raw_name
            if raw_cat in 'Helicopters':
                cat = 'Helicopter'
                if raw_name in l_HELO:
                    name = raw_name
                else:
                    if raw_name in d_HELOS.keys():
                        name = d_HELOS[raw_name]
                    else:
                        print 'unkown raw_name: %s' % raw_name
            if raw_cat in 'Cars':
                if raw_name in l_SAM:
                    cat = 'SAM'
                    name = raw_name
                elif raw_name in l_TEC:
                    cat = 'Vehicle'
                    name = raw_name
                elif raw_name in d_SAM.keys():
                    cat = 'SAM'
                    name = d_SAM[raw_name]
                elif raw_name in d_TEC.keys():
                    cat = 'Vehicle'
                    name = d_TEC[raw_name]
                elif raw_name in d_IGNORE:
                    pass
                else:
                    print 'unkown raw_name: %s' % raw_name
            l = '''insert into country_forces (country, category, unit) values ('{}', '{}', '{}');'''.format(cur_cnt_id, cat, name)
            if not l in output:
                output.append(l)

with open(OUT_FILE, mode='w') as f:
    for x in output:
        f.write('{}\n'.format(x))
