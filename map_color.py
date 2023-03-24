from PIL import Image
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def color_map_gradient(width, height, stations, image, num_pixels):
    for i in range(width):
        for j in range(height):
            r, g, b, v = image.getpixel((i,j))
            min_val = 1000000000000
            if r==0:
                continue
            for (x,y) in stations:
                min_val = min(min_val, get_distance(i,j,x+3,y+3))
            if min_val > num_pixels:
                image.putpixel((i, j), (r, 0 , 0, v))
            else:
                image.putpixel((i, j), (round((r/num_pixels)*min(num_pixels,2*min_val)), round((g/num_pixels)*min(num_pixels,2*(150-min_val))) , 0, v))

broad_street_stations = [
    (758,2424), # NRG
    (778,2299), # Oregon
    (790,2228), # Snyder
    (798,2163), # Tasker Morris
    (810,2097), # Ellsworth Federal
    (823,2013), # Lombard South
    (831,1964), # Walnut Locust
    (833,1919), # City Hall
    (846,1880), # Race Vine
    (855,1822), # Spring Garden
    (863,1775), # Fairmount
    (871,1726), # Girard
    (884,1652), # Cecil B Moore
    (899,1563), # Sesquehanna Dauphin
    (912,1483), # North Philadelphia
    (924,1411), # Allegheny
    (937,1330), # Erie
    (952,1243), # Hunting Park
    (964,1169), # Wyoming
    (974,1114), # Logan
    (989,1020), # Olney
    (1053,988), # Fern Rock
    (921,1890) # Chinatown
]

mfl_stations = [
    (1528,1184), # Frankford
    (1477,1255), # Arrott
    (1438,1316), # Church
    (1381,1364), # Erie-Torresdale
    (1296,1425), # Tioga
    (1241,1464), # Allegheny
    (1169,1516), # Somerset
    (1130,1544), # Huntingdon
    (1091,1583), # York-Dauphin
    (1079,1653), # Berks
    (1058,1754), # Girard
    (1025,1842), # Spring Garden
    (997,1952), # 2nd St
    (956,1946), # 5th St
    (919,1939), # 8th St
    (881,1935), # 11th St
    (854,1929), # 13th St
    (678,1899), # 30th St
    (613,1890), # 34th St
    (530,1876), # 40th St
    (432,1861), # 46th St
    (345,1847), # 52nd St
    (281,1837), # 56th St
    (217,1826), # 60th St
    (169,1819), # 63rd St
    (125,1801), # Millbourne
    (70,1821),  # 69th St

    #PROPOSED ADDITIONAL
    (742,1910), # Comcast Center
]

regional_rail_stations = [
    (691,1890), # 30th St
    (883,1923), # Jefferson
    (807,1908), # Suburban
    
    (623,1975), # Penn Medicine
    (106,2341), # Darby
    (22,2392),  # Curtis Park
    (184,2563), # Eastwick
    (94,2061),  # Fernwood Yeadon
    (237,2005), # Angora
    (411,2019), # 49th St
    (338,1528), # Wynnefield
    (321,1417), # Bala
    (287,1357), # Cynwyd
    (143,1534), # Overbrook
    (130,1453), # Merion
    (50,1377),  # Narberth

    (951,1621), # Temple
    (916,1509), # North Broad St
    (905,1456), # North Philadelphia
    (823,1388), # Allegheny
    (609,1307), # East Falls
    (463,1253), # Wissahickon
    (343,1144), # Manayunk
    (260,1068), # Ivy Ridge
    (12,812), # Miquon

    (868,1189), # Wayne Junction
    (1069,993), # Fern Rock T-C
    (1115,803), # Melrose
    (1125,679), # Elkins Park
    (1044,449), # Jenkintown
    (917,362),  # Glenside
    (787,249),  # North Hills
    (675,187),  # Oreland
    (450,5),# Fort Washington
    (1151,330), # Noble
    (1263,298), # Rydal
    (1411,259), # Meadowbrook
    (1607,203), # Bethayres
    (1801,146), # Philmont
    (1985,84),  # Forest Hills
    (2056,54),  # Somerton
    (1168,1076), # Olney
    (1323,888), # Lawndale
    (1406,819), # Cheltenham
    (1455,760), # Ryers
    (1481,629), # Fox Chase

    (922,228),  # Ardsley
    (1075,158), # Roslyn
    (1201,28),  # Crestmont

    (1591,1315), # Bridesburg
    (1840,1183), # Tacony
    (1962,1082), # Holmesburg
    (2278,856),  # Torresdale

    (855,1046), # Wister
    (771,1030), # Germantown
    (773,891),  # Washington Lane
    (714,791),  # Stenton
    (663,766),  # Sedgwick
    (616,743),  # Mt. Airy
    (571,656),  # Wyndmoor
    (529,615),  # Gravers
    (483,577),  # Chestnut Hill East

    (724,1183), # Queen Lane
    (697,1114), # Chelten Avenue
    (651,1058), # Tulpehocken
    (625,982),  # Upsal
    (612,891),  # Carpenter
    (586,824),  # Richard Allen Lane
    (508,737),  # St. Martins
    (458,691),  # Highland
    (478,627), # Chestnut Hill West
]

patco_and_rvln_stations = [

]

roosevelt_blvd_extension_stations = [
    (1030,1203), # 9th St
    (1083,1177), # 5th St
    (1173,1156), # Rising Sun
    (1353,1132), # Adams
    (1472,1093), # Oxford Circle
    (1587,1059), # Bustleton
    (1724,951),  # Cottman
    (1796,807),  # Pennypack Circle
    (1873,646),  # Welsh Grant
    (2031,431),  # Red Lion
    (2143,326),  # Comly
    (2266,215)   # Southampton
]

schuylkill_snyder_line_concept_stations = [
    (730,1379), # Allegheny
    (718,1460), # Lehigh
    (707,1523), # Dauphin
    (692,1620), # Cecil B Moore
    (677,1695), # Girard
    (711,1780), # Art Museum
    (734,1910), # Comcast Center
    (719,2003), # Fitler Square
    (667,2055), # Grays Ferry
    (654,2135), # Tasker-Morris
    (643,2197), # Smith Playground
    (700,2207), # 21st St
    (751,2216), # 17th St
    (790,2224), # Broad St
    (841,2231), # 10th St
    (884,2239), # 5th St
    (926,2237), # Moyamensing
    # (1002,2266), # Pennsport
    (940,2192),
    (955,2132),
    (968,2047),
    (981,1960)
]

im = Image.open("philadelphia_blackout.png")
width, height = im.size
print(width)
print(height)
colortuples = im.getcolors()
dark = min(colortuples)[1]
black = max(colortuples)[1]
print(dark)
print(black)
pix = im.load()
all_stations = broad_street_stations + mfl_stations + regional_rail_stations + roosevelt_blvd_extension_stations + schuylkill_snyder_line_concept_stations

# Coloring
color_map_gradient(width,height,all_stations,im,150)


# Stations
for (x,y) in broad_street_stations + roosevelt_blvd_extension_stations:
    print(x,y)
    for i in range(8):
        for j in range(8):
            im.putpixel((x+i, y+j), (253, 73 , 2, 255))

for (x,y) in mfl_stations:
    print(x,y)
    for i in range(8):
        for j in range(8):
            im.putpixel((x+i, y+j), (0, 107, 182, 255))

for (x,y) in regional_rail_stations:
    print(x,y)
    if im.getpixel((x,y)) != black:
        for i in range(8):
            for j in range(8):
                im.putpixel((x+i, y+j), (25, 25, 112, 255))

for (x,y) in schuylkill_snyder_line_concept_stations:
    print(x,y)
    for i in range(8):
        for j in range(8):
            im.putpixel((x+i, y+j), (75, 0, 130, 255))

im.save('MyImage.png')