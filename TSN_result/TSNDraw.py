import matplotlib.pyplot as plt

x = [400,440,480,520,560,600,640,680,720,760,800,840,880,920,960,1000,1040,1080,1120,1160,1200,1240,1280,1320,1360,1400,1440,1480,1520,1560,1600,1640,1680,1720,1760,1800,1840,1880,1920,1960,2000,2040,2080,2120,2160,2200,2240,2280,2320,2360,2400,2440,2480,2520,2560,2600,2640,2680,2720,2760,2800,2840,2880,2920,2960,3000]
ECMP1 = [400,440,480,520,560,600,640,680,720,760,796,836,876,916,956,996,1036,1076,1116,1156,1192,1232,1272,1312,1352,1392,1432,1472,1512,1552,1588,1628,1668,1708,1748,1788,1828,1868,1908,1948,1984,2024,2064,2104,2144,2184,2224,2264,2304,2344,2380,2420,2460,2500,2540,2580,2620,2660,2684,2704,2722,2735,2735,2735,2735,2735]
SrmACO1 = [400,440,480,520,560,600,640,680,720,760,797,836,878,918,957,997,1038,1079,1117,1157,1193,1234,1274,1314,1355,1394,1433,1475,1514,1515,1590,1630,1669,1711,1749,1791,1829,1869,1910,1952,1986,2027,2066,2105,2145,2186,2226,2265,2305,2346,2382,2423,2361,2501,2466,2269,2623,2651,2289,2404,2643,2219,2614,2898,2194,2092]
CCPK1 = [400,440,480,520,560,600,640,680,720,760,800,840,880,920,960,1000,1040,1080,1120,1160,1196,1236,1276,1316,1356,1396,1436,1476,1516,1556,1592,1632,1672,1712,1752,1792,1832,1872,1912,1952,1988,2028,2068,2108,2148,2188,2228,2268,2308,2348,2376,2396,2416,2429,2429,2429,2429,2429,2429,2429,2429,2429,2429,2429,2429,2429]
FCPS1 = [400,440,480,520,560,600,640,680,720,760,799,838,879,918,958,998,1040,1079,1119,1160,1197,1237,1277,1317,1357,1397,1437,1477,1517,1556,1593,1633,1673,1713,1753,1793,1833,1873,1913,1952,1989,2029,2069,2109,2149,2189,2229,2269,2309,2349,2385,2425,2465,2505,2545,2585,2625,2665,2705,2745,2781,2821,2856,2856,2856,2856]
l1 = plt.plot(x, ECMP1, color='red', marker='o', label='ECMP')
l2 = plt.plot(x, CCPK1, color='black', marker='o', label='CCPK')
l3 = plt.plot(x, SrmACO1, color='blue', marker='o', label='SrmACO')
l4 = plt.plot(x, FCPS1, color='green', marker='o', label='FCPS')
plt.plot(x, ECMP1, 'red', x, CCPK1, 'black', x, SrmACO1, 'blue', x, FCPS1, 'green')
plt.title('Total number of data streams')
plt.xlabel('count')
plt.ylabel('count')
plt.legend()
plt.show()

ECMP2 = [1510.4,1534.72,1559.04,1583.36,1607.68,1632,1656.32,1680.64,1704.96,1729.28,1740.8,1765.12,1789.44,1813.76,1838.08,1862.4,1886.72,1911.04,1935.36,1959.68,1971.2,1995.52,2019.84,2044.16,2068.48,2092.8,2117.12,2141.44,2165.76,2190.08,2201.6,2225.92,2250.24,2274.56,2298.88,2323.2,2347.52,2371.84,2396.16,2420.48,2432,2456.32,2480.64,2504.96,2529.28,2553.6,2577.92,2602.24,2626.56,2650.88,2662.4,2686.72,2711.04,2735.36,2759.68,2784,2808.32,2832.64,2839.552,2844.416,2846.72,2848.384,2848.384,2848.384,2848.384,2848.384]
SrmACO2 = [1510.4,1534.72,1559.04,1583.36,1607.68,1632,1656.32,1680.64,1704.96,1729.28,1868.8,1765.12,2429.44,2069.76,1966.08,1606.4,2142.72,2679.04,2063.36,2087.68,2099.2,2251.52,2275.84,2300.16,2836.48,2348.8,2245.12,2909.44,2421.76,2549.76,2841.6,2865.92,2762.24,2658.56,2810.88,2707.2,2475.52,2499.84,2652.16,3316.48,2688,2840.32,2736.64,2632.96,2657.28,2809.6,2449.92,2730.24,2754.56,2906.88,2918.4,3454.72,3295.104,2863.36,3468.288,3233.024,3576.32,2700.928,2881.92,3084.8,2942.976,3331.456,3049.856,3221.76,2952.32,2924.672]
CCPK2 = [1510.4,1534.72,1559.04,1583.36,1607.68,1632,1656.32,1680.64,1704.96,1729.28,3020.8,3045.12,3069.44,3093.76,3118.08,3142.4,3166.72,3191.04,3215.36,3239.68,3251.2,3275.52,3299.84,3324.16,3348.48,3372.8,3397.12,3421.44,3445.76,3470.08,3481.6,3505.92,3530.24,3554.56,3578.88,3603.2,3627.52,3651.84,3676.16,3700.48,3712,3736.32,3760.64,3784.96,3809.28,3833.6,3857.92,3882.24,3906.56,3930.88,3938.304,3943.168,3948.032,3949.696,3949.696,3949.696,3949.696,3949.696,3949.696,3949.696,3949.696,3949.696,3949.696,3949.696,3949.696,3949.696]
FCPS2 = [1510.4,1534.72,1559.04,1583.36,1607.68,1632,1656.32,1680.64,1704.96,1729.28,2892.8,2405.12,2941.44,2453.76,2478.08,2502.4,3166.72,3063.04,3087.36,3239.68,3763.2,3787.52,3811.84,3836.16,3860.48,3884.8,3909.12,3933.44,3957.76,3470.08,3993.6,4017.92,4042.24,4066.56,4090.88,4115.2,4139.52,4163.84,4188.16,3700.48,4224,4248.32,4272.64,4296.96,4321.28,4345.6,4369.92,4394.24,4418.56,4442.88,4454.4,4478.72,4503.04,4527.36,4551.68,4576,4600.32,4624.64,4648.96,4673.28,4684.8,4709.12,4721.28,4725.888,4725.888,4725.888]
l1 = plt.plot(x, ECMP2, color='red', marker='o', label='ECMP')
l2 = plt.plot(x, CCPK2, color='black', marker='o', label='CCPK')
l3 = plt.plot(x, SrmACO2, color='blue', marker='o', label='SrmACO')
l4 = plt.plot(x, FCPS2, color='green', marker='o', label='FCPS')
plt.plot(x, ECMP2, 'red', x, CCPK2, 'black', x, SrmACO2, 'blue', x, FCPS2, 'green')
plt.title('total bytes')
plt.xlabel('count')
plt.ylabel('MB')
plt.legend()
plt.show()

ECMP3 = [1510.4,1395.2,1299.2,1217.969231,1148.342857,1088,1035.2,988.611765,947.2,910.147368,874.773869,844.555024,817.09589,792.034934,769.07113,747.951807,728.46332,710.423792,693.677419,678.089965,661.47651,647.896104,635.169811,623.219512,611.976331,601.37931,591.374302,581.913043,572.952381,564.453608,554.559194,546.909091,539.625899,532.683841,526.059497,519.731544,513.680525,507.888651,502.339623,497.01848,490.322581,485.438735,480.744186,476.228137,471.880597,467.692308,463.654676,459.759717,456,452.368601,447.462185,444.08595,440.819512,437.6576,434.595276,431.627907,428.751145,425.960902,424.701167,424.159857,423.367043,422.797091,422.797091,422.797091,422.797091,422.797091]
SrmACO3 = [1510.4,1395.2,1299.2,1217.969231,1148.342857,1088,1035.2,988.611765,947.2,910.147368,938.623807,844.555024,1106.806378,903.036649,822.283563,645.659164,826.666667,993.709199,739.290577,722.130751,704.193224,730.538611,715.22313,700.840951,837.70821,674.554854,626.953365,789.321758,640.338445,674.004758,714.867925,703.293252,661.77288,622.176457,642.633745,605.231388,541.570772,535.183044,555.775356,680.024605,541.71705,560.995457,530.151104,500.467592,495.668719,514.390333,440.712358,482.289348,478.139212,495.885363,490.322581,570.462351,558.681587,458.06431,562.851022,568.893894,545.503356,406.888822,497.483169,503.476416,445.702862,601.020386,467.124521,444.871582,483.273858,490.305448]
CCPK3 = [1510.4,1395.2,1299.2,1217.969231,1148.342857,1088,1035.2,988.611765,947.2,910.147368,1510.4,1450.057143,1395.2,1345.113043,1299.2,1256.96,1217.969231,1181.866667,1148.342857,1117.131034,1087.35786,1060.038835,1034.432602,1010.382979,987.752212,966.418338,946.272981,927.219512,909.171504,892.051414,874.773869,859.294118,844.555024,830.504673,817.09589,804.285714,792.034934,780.307692,769.07113,758.295082,746.881288,736.946746,727.396518,718.208729,709.363128,700.840951,692.624776,684.698413,677.046794,669.655877,664.356275,662.940148,661.533512,660.373851,660.373851,660.373851,660.373851,660.373851,660.373851,660.373851,660.373851,660.373851,660.373851,660.373851,660.373851,660.373851]
FCPS3 = [1510.4,1395.2,1299.2,1217.969231,1148.342857,1088,1035.2,988.611765,947.2,910.147368,1447.123562,1148.02864,1337.626194,1069.176471,1034.688935,1002.965932,1217.969231,1134.879585,1103.022508,1117.131034,1256.913828,1224.149968,1193.437696,1164.590164,1137.442546,1111.848884,1087.679466,1064.818625,1043.162889,892.051414,1002.409639,983.819785,966.118547,949.243697,933.138686,917.752007,903.036649,888.949616,875.451505,758.295082,849.215923,837.272369,825.790491,814.744027,804.108671,793.861893,783.982777,774.451886,765.251126,756.363636,746.881288,738.575198,730.538611,722.758621,715.22313,707.920792,700.840951,693.973589,687.309284,680.839161,673.684211,667.581514,661.243697,661.889076,661.889076,661.889076]
l1 = plt.plot(x, ECMP3, color='red', marker='o', label='ECMP')
l2 = plt.plot(x, CCPK3, color='black', marker='o', label='CCPK')
l3 = plt.plot(x, SrmACO3, color='blue', marker='o', label='SrmACO')
l4 = plt.plot(x, FCPS3, color='green', marker='o', label='FCPS')
plt.plot(x, ECMP3, 'red', x, CCPK3, 'black', x, SrmACO3, 'blue', x, FCPS3, 'green')
plt.title('Average bytes of data stream')
plt.xlabel('count')
plt.ylabel('KB/Stream')
plt.legend()
plt.show()

ECMP4 = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
SrmACO4 = [4,4,4,4,4,4,4,4,4,4,5,4,6,6,5,5,6,7,5,5,5,6,6,6,7,6,5,7,6,7,6,6,5,7,5,7,5,5,6,8,6,7,6,5,5,6,6,5,5,6,6,7,6,5,7,6,7,6,6,7,5,7,6,6,6,6]
CCPK4 = [4,4,4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
FCPS4 = [4,4,4,4,4,4,4,4,4,4,7,6,7,6,6,6,8,7,7,8,9,9,9,9,9,9,9,9,9,8,9,9,9,9,9,9,9,9,9,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
l1 = plt.plot(x, ECMP4, color='red', marker='o', label='ECMP')
l2 = plt.plot(x, CCPK4, color='black', marker='o', label='CCPK')
l3 = plt.plot(x, SrmACO4, color='blue', marker='o', label='SrmACO')
l4 = plt.plot(x, FCPS4, color='green', marker='o', label='FCPS')
plt.plot(x, ECMP4, 'red', x, CCPK4, 'black', x, SrmACO4, 'blue', x, FCPS4, 'green')
plt.title('The number of successful large flow scheduling')
plt.xlabel('count')
plt.ylabel('count')
plt.legend()
plt.show()

ECMP5 = [1,1,1,1,1,1,1,1,1,1,0.995,0.995238,0.995455,0.995652,0.995833,0.996,0.996154,0.996296,0.996429,0.996552,0.993333,0.993548,0.99375,0.993939,0.994118,0.994286,0.994444,0.994595,0.994737,0.994872,0.9925,0.992683,0.992857,0.993023,0.993182,0.993333,0.993478,0.993617,0.99375,0.993878,0.992,0.992157,0.992308,0.992453,0.992593,0.992727,0.992857,0.992982,0.993103,0.99322,0.991667,0.991803,0.991935,0.992063,0.992188,0.992308,0.992424,0.992537,0.986765,0.97971,0.972143,0.963028,0.949653,0.936644,0.923986,0.911667]
SrmACO5 = [1,1,1,1,1,1,1,1,1,1,0.99625,0.995238,0.997727,0.997826,0.996875,0.997,0.998077,0.999074,0.997321,0.997414,0.994167,0.995161,0.995313,0.995455,0.996324,0.995714,0.995139,0.996622,0.996053,0.996711,0.99375,0.993902,0.993452,0.994767,0.99375,0.995,0.994022,0.994149,0.994792,0.995918,0.993,0.993627,0.993269,0.992925,0.993056,0.993636,0.99375,0.993421,0.993534,0.994068,0.9925,0.993033,0.952016,0.99246,0.963281,0.872692,0.993561,0.989179,0.841544,0.883824,0.943929,0.781338,0.907639,0.992466,0.741216,0.697333]
CCPK5 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.996667,0.996774,0.996875,0.99697,0.997059,0.997143,0.997222,0.997297,0.997368,0.997436,0.995,0.995122,0.995238,0.995349,0.995455,0.995556,0.995652,0.995745,0.995833,0.995918,0.994,0.994118,0.994231,0.99434,0.994444,0.994545,0.994643,0.994737,0.994828,0.994915,0.99,0.981967,0.974194,0.963889,0.948828,0.934231,0.920076,0.906343,0.893015,0.880072,0.8675,0.855282,0.843403,0.831849,0.820608,0.809667]
FCPS5 = [1,1,1,1,1,1,1,1,1,1,0.99875,0.997619,0.998864,0.997826,0.997917,0.998,1,0.999074,0.999107,1,0.9975,0.997581,0.997656,0.997727,0.997794,0.997857,0.997917,0.997973,0.998026,0.997436,0.995625,0.995732,0.995833,0.99593,0.996023,0.996111,0.996196,0.996277,0.996354,0.995918,0.9945,0.994608,0.994712,0.994811,0.994907,0.995,0.995089,0.995175,0.995259,0.995339,0.99375,0.993852,0.993952,0.994048,0.994141,0.994231,0.994318,0.994403,0.994485,0.994565,0.993214,0.99331,0.991667,0.978082,0.964865,0.952]
l1 = plt.plot(x, ECMP5, color='red', marker='o', label='ECMP')
l2 = plt.plot(x, CCPK5, color='black', marker='o', label='CCPK')
l3 = plt.plot(x, SrmACO5, color='blue', marker='o', label='SrmACO')
l4 = plt.plot(x, FCPS5, color='green', marker='o', label='FCPS')
plt.plot(x, ECMP5, 'red', x, CCPK5, 'black', x, SrmACO5, 'blue', x, FCPS5, 'green')
plt.title('Success rate')
plt.xlabel('count')
plt.ylabel('%')
plt.legend()
plt.show()

ECMP6 = [77,233,363,472,563,642,709,768,819,865,900,935,966,995,1031,1064,1093,1119,1142,1163,1180,1196,1211,1223,1235,1245,1276,1306,1333,1358,1378,1398,1416,1432,1446,1459,1469,1479,1486,1493,1498,1502,1505,1507,1508,1508,1507,1505,1503,1499,1496,1491,1486,1481,1475,1469,1462,1455,1452,1451,1450,1449,1449,1449,1449,1449]
SrmACO6 = [73,75,233,468,84,417,434,786,570,610,953,508,812,681,1094,1051,312,804,1247,1444,1808,1094,1023,1566,1039,1099,504,911,1041,920,1235,1619,668,981,746,1599,869,1726,1043,943,1285,1084,1697,1219,907,750,317,1196,1091,1228,989,934,1503,1300,1000,1520,686,889,1382,1194,711,1159,937,370,1499,1637]
CCPK6 = [76,586,1006,1336,1360,1387,1388,1415,1409,1428,1441,1547,1647,1736,1816,1865,1918,1964,2005,2040,2063,2038,2061,2060,2057,2055,2054,2036,2032,2027,2021,2014,2001,1982,1964,1938,1914,1890,1866,1844,1825,1804,1789,1773,1764,1753,1740,1727,1713,1694,1685,1684,1683,1683,1683,1683,1683,1683,1683,1683,1683,1683,1683,1683,1683,1683]
FCPS6 = [71,76,77,74,67,60,57,55,54,52,166,151,153,142,137,133,159,138,137,166,220,237,259,264,283,295,301,303,309,301,389,386,376,372,371,378,374,374,272,414,432,434,431,426,425,424,418,414,409,403,396,391,386,380,374,371,366,362,358,353,346,341,337,337,338,338]
l1 = plt.plot(x, ECMP6, color='red', marker='o', label='ECMP')
l2 = plt.plot(x, CCPK6, color='black', marker='o', label='CCPK')
l3 = plt.plot(x, SrmACO6, color='blue', marker='o', label='SrmACO')
l4 = plt.plot(x, FCPS6, color='green', marker='o', label='FCPS')
plt.plot(x, ECMP6, 'red', x, CCPK6, 'black', x, SrmACO6, 'blue', x, FCPS6, 'green')
plt.title('Average delay of data flow (ms)')
plt.xlabel('count')
plt.ylabel('ms')
plt.legend()
plt.show()

ECMP7 = [149,224,305,349,383,255,455,513,541,630,629,665,697,1183,782,875,957,963,926,1080,1102,1010,1458,1348,1268,1177,1164,2043,1243,1313,1408,1447,1496,1685,1503,1477,1855,1925,1510,1473,1720,1745,1697,1783,1676,1668,1640,1827,1705,1932,1866,2245,2319,1849,2267,2032,2028,1851,2154,2144,2302,2379,2173,2144,1980,2473]
SrmACO7 = [840,960,1006,959,864,1042,1009,1130,1222,1341,1881,1686,1851,1753,1602,1598,1790,2146,1913,1830,2526,2210,2446,2414,2432,2539,2156,2328,2376,2289,3878,3437,2782,2841,2818,3197,2768,3426,3961,3254,3336,3355,3361,3219,3881,3115,2636,3828,3164,3527,3491,4920,4664,3679,3526,4195,3866,3763,4291,3943,4190,4133,3978,3785,4405,4663]
CCPK7 = [338,372,392,537,589,788,781,801,880,946,949,1026,1209,1411,1492,1481,1604,1468,1641,1946,1855,1859,2632,2565,2254,2254,2304,2216,2606,2324,2607,2775,2785,2725,2417,2596,2764,2884,2798,2791,2809,2749,2978,2862,3032,3009,3161,3023,3161,3277,3435,3703,4029,3511,3555,3878,3524,3532,3901,3882,3788,3841,3833,4360,4610,4400]
FCPS7 = [233,268,247,303,314,327,312,303,353,369,494,561,518,555,643,637,597,682,734,710,733,777,924,856,972,846,1001,941,941,926,970,780,1013,1063,817,1097,1276,1162,1172,1103,1171,1199,1152,1302,1380,1288,1350,970,1304,1310,1337,1385,1636,1537,1422,1471,1531,1453,1594,1588,1774,1506,1597,1548,1727,1520]
l1 = plt.plot(x, ECMP7, color='red', marker='o', label='ECMP')
l2 = plt.plot(x, CCPK7, color='black', marker='o', label='CCPK')
l3 = plt.plot(x, SrmACO7, color='blue', marker='o', label='SrmACO')
l4 = plt.plot(x, FCPS7, color='green', marker='o', label='FCPS')
plt.plot(x, ECMP7, 'red', x, CCPK7, 'black', x, SrmACO7, 'blue', x, FCPS7, 'green')
plt.title('Algorithm scheduling time (ms)')
plt.xlabel('count')
plt.ylabel('ms')
plt.legend()
plt.show()