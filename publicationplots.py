"""

@author: Zarina Dhillon
"""
import matplotlib.pyplot as plt
import numpy as np
#%%
la_data=np.asarray([1,           1.00356961,     1.00356961,     1.00407955,
     1.00484447,     1.00484447,     1.00586435,     1.00790413,
     1.00790413,     1.01019888,     1.01223865,     1.01223865,
     1.01733809,     1.01733809,     1.03008669,     1.04563998,
     1.04563998,     1.07011729,     1.10581336,     1.10581336,
     1.14686384,     1.21468638,     1.21468638,     1.29576747,
     1.41279959,     1.41279959,    1.55354411,     1.55354411,
     1.73610403,     1.96175421,     1.96175421,     2.24604793,
     2.5917899,      2.5917899,      3.00866905,     3.49847017,
     3.49847017,     4.08057114,     4.08057114,     4.77460479,
     5.60989291,     5.60989291,     6.59765426,     7.736359,
     7.736359,       9.02830189,    10.51300357,    10.51300357,
    12.20295767,    14.16955635,    14.16955635,    16.39214686,
    16.39214686,    18.94951555,    21.85262621,    21.85262621,
    25.12850586,    28.92350841,    28.92350841,    33.2781744,
    38.3072412,     38.3072412,     44.10963794,    44.10963794,
    50.8809281,     58.82585416,    58.82585416,    68.16649669,
    79.35313616,    79.35313616,    92.70576237,   108.97042325,
   108.97042325,   128.75879653,   153.30112188,   153.30112188,
   183.67134115,   183.67134115,   221.90744518,   269.85466599,
   269.85466599,   329.81132075,   404.16496685,   404.16496685,
   497.45767466,   615.22870984,   615.22870984,   766.72565018,
   766.72565018,   963.07062723,  1225.28939317,  1225.28939317,
  1589.66369199,  2123.20193779,  2123.20193779,  2957.1573177,
  4375.53977562,  4375.53977562,  7367.74757777, 27859.00764916])

null_data=np.asarray([1,	1.00382458,	1.00382458,	1.00433452,	1.00509944,	1.00509944,	1.00611933,	1.0081591,	1.0081591,	1.01019888,	1.01223865,	1.01223865,	1.01733809,	1.01733809,	1.02957675,	1.042095867,	1.042095867,	1.061779701,	1.085492095,	1.085492095,	1.111167771,	1.154487508,	1.154487508,	1.203569606,	1.269658338,	1.269658338,	1.350866906,	1.350866906,	1.455048444,	1.579933708,	1.579933708,	1.746149925,	1.966241714,	1.966241714,	2.233350333,	2.559433962,	2.559433962,	2.964788374,	2.964788374,	3.46137175,	4.058643549,	4.058643549,	4.777383987,	5.626746558,	5.626746558,	6.630494644,	7.808643548,	7.808643548,	9.180877103,	10.77914329,	10.77914329,	12.61065783,	12.61065783,	14.71868944,	17.14337073,	17.14337073,	19.93151453,	23.15155533,	23.15155533,	26.85627231,	31.17029577,	31.17029577,	36.19938807,	36.19938807,	42.12774095,	49.14750128,	49.14750128,	57.54487506,	67.71927588,	67.71927588,	79.99668537,	95.08006119,	95.08006119,	113.7168027,	137.1487251,	137.1487251,	166.5555329,	166.5555329,	204.0401071,	252.0314125,	252.0314125,	313.6069097,	392.0557114,	392.0557114,	492.4525242,	620.3994136,	620.3994136,	784.181948,	784.181948,	995.9106578,	1274.921775,	1274.921775,	1654.530393,	2188.918383,	2188.918383,	2993.323151,	4342.571163,	4342.571163,	7239.739903,	31438.04941]
                     )

difference_la_null=np.asarray([0,	0.00025497,	0.00025497,	0.00025497,	0.00025497,	0.00025497,	0.00025498,	0.00025497,	0.00025497,	0,	0,	0,	0,	0,	0.00050994,	0.003544113,	0.003544113,	0.008337589,	0.020321265,	0.020321265,	0.035696069,	0.060198872,	0.060198872,	0.092197864,	0.143141252,	0.143141252,	0.202677204,	0.202677204,	0.281055586,	0.381820502,	0.381820502,	0.499898005,	0.625548186,	0.625548186,	0.775318717,	0.939036208,	0.939036208,	1.115782766,	1.115782766,	1.31323304,	1.551249361,	1.551249361,	1.820270273,	2.109612442,	2.109612442,	2.397807246,	2.704360022,	2.704360022,	3.022080567,	3.390413056,	3.390413056,	3.781489033,	3.781489033,	4.230826106,	4.709255481,	4.709255481,	5.196991326,	5.771953081,	5.771953081,	6.421902089,	7.136945434,	7.136945434,	7.910249872,	7.910249872,	8.753187151,	9.678352884,	9.678352884,	10.62162163,	11.63386028,	11.63386028,	12.709077,	13.89036206,	13.89036206,	15.04199388,	16.15239674,	16.15239674,	17.11580826,	17.11580826,	17.86733809,	17.82325345,	17.82325345,	16.20441101,	12.10925548,	12.10925548,	5.005150438,	5.170703724,	5.170703724,	17.45629781,	17.45629781,	32.8400306,	49.63238144,	49.63238144,	64.86670067,	65.71644569,	65.71644569,	36.16583375,	32.96861295,	32.96861295,	128.0076747,	3579.041764])

difference_subnulls=np.asarray([0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.000050994,	0.000050994,	0.000118986,	0.0001869833333,	0.0001869833333,	0.000339962,	0.0003796275556,	0.0003796275556,	0.0008385746667,	0.001801802667,	0.001801802667,	0.002181426222,	0.002181426222,	0.002997337333,	0.003926567556,	0.003926567556,	0.007365856667,	0.005484730667,	0.005484730667,	0.01120743311,	0.01082781111,	0.01082781111,	0.007042892889,	0.007042892889,	0.016131224,	0.02251685889,	0.02251685889,	0.03096492556,	0.03378661644,	0.03378661644,	0.03789449867,	0.04736245778,	0.04736245778,	0.06071732022,	0.06508017511,	0.06508017511,	0.08772168289,	0.08772168289,	0.09793756089,	0.1110601167,	0.1110601167,	0.147668424,	0.1805654722,	0.1805654722,	0.207450846,	0.2620261773,	0.2620261773,	0.3356450791,	0.3356450791,	0.409994902,	0.5255538582,	0.5255538582,	0.6667573247,	0.9140347889,	0.9140347889,	1.20375092,	1.544903393,	1.544903393,	1.976502918,	2.580843105,	2.580843105,	3.505853022,	3.505853022,	4.734959487,	6.990707688,	6.990707688,	10.22137798,	14.71589892,	14.71589892,	20.39623775,	28.03646099,	28.03646099,	39.14702249,	39.14702249,	54.71887359,	76.34217236,	76.34217236,	110.6929004,	163.3637996,	163.3637996,	251.5744235,	405.2041872,	405.2041872,	732.7082384,	5413.514035])
#%%
# ORIGINAL PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim()
plt.xlim()
ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
ax.plot(null_data, marker='.', label='Null Model', color='C3')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Time (number of steps)')
plt.savefig('og_pubthesis_plot.png', dpi=600)
plt.show()
#%%
## EARLY ZOOMED IN PLOT
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
# })
# fig, ax=plt.subplots()
# plt.ylim(0, 15)
# plt.xlim(30, 50)
# ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
# ax.plot(null_data, marker='.', label='Null Model', color='C3')
# ax.legend(loc='upper left')
# ax.set_xlabel('Percent of Classes seen')
# ax.set_ylabel('Time (number of steps)')
# #plt.savefig('early_zoom_thesis_plot.png', dpi=600)
# plt.show()
#%%
## LATE ZOOMED IN PLOT
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
# })
# fig, ax=plt.subplots()
# plt.ylim(2000, 30000)
# plt.xlim(95, 99)
# ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
# ax.plot(null_data, marker='.', label='Null Model', color='C3')
# ax.legend(loc='upper left')
# ax.set_xlabel('Percent of Classes seen')
# ax.set_ylabel('Time (number of steps)')
# #plt.savefig('zoom_thesis_plot.png', dpi=600)
# plt.show()
#%%
## TIME BOUNDED ZOOMED IN PLOT
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
# })
# fig, ax=plt.subplots()
# plt.ylim(2750, 4500)
# plt.xlim(95, 97)
# ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
# ax.plot(null_data, marker='.', label='Null Model', color='C3')
# ax.legend(loc='upper left')
# ax.set_xlabel('Percent of Classes seen')
# ax.set_ylabel('Time (number of steps)')
# #plt.savefig('zoom_zoom_thesis_plot.png', dpi=600)
# plt.show()
#%%
## LOG PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim()
plt.xlim()
ax.plot(np.log(la_data), marker='.', label='Los Angeles', color='C9')
ax.plot(np.log(null_data), marker='.', label='Null Model', color='C3')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Log(Time)')
plt.savefig('log_pubthesis_plot.png', dpi=600)
plt.show()
#%%
# DIFFERENCE PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim()
plt.xlim()
ax.plot(np.log(difference_la_null), marker='.', label='Difference between LA County and null model', color='black')
ax.plot(np.log(difference_subnulls), marker='.', label='Average difference between sub-null models', color='grey')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Log(Time)')
plt.savefig('diffs_log_pubthesis_plot.png', dpi=600)
plt.show()
invalid=np.where(difference_subnulls==0)
print(invalid)
#%%
## BOX PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim(9, 16)
plt.xlim(48.5, 51.5)
ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
ax.plot(null_data, marker='.', label='Null Model', color='C3')
ax.axhspan(10.623, 10.831, xmin=0.156, xmax=0.51, alpha=0.1, color='C3')
ax.axhspan(12.432, 12.687, xmin=0.824, alpha=0.1, color='C3')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Time (number of steps)')
plt.savefig('range_shaded_pubthesis_plot.png', dpi=600)
plt.show()
# print(la_data[50])
# print(null_data[50])
#10 sub-null models at [50]=
#%%
## DIFFERENCE BOX PLOT
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
# })
# fig, ax=plt.subplots()
# plt.ylim()
# plt.xlim(97, 99)
# #ten_null_50=np.asarray([10, 10, 10, 9.8, 9.9, 10.1, 10.1, 10, 10, 10.1])
# ax.plot(difference_la_null, marker='.', label='Difference between LA County and null model', color='black')
# ax.plot(difference_subnulls, marker='.', label='Average difference between sub-null models', color='grey')
# ax.axhspan(7.9, 867.3, xmin=0.45, xmax=0.55, alpha=0.1, color='grey')
# ax.legend(loc='upper left')
# ax.set_xlabel('Percent of Classes seen')
# ax.set_ylabel('Log(Time) (number of steps)')
# #plt.savefig('range_shaded_thesis_plot.png', dpi=600)
# plt.show()
#%%
## LAST ZOOM FOR DIFFERENCE
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
# })
# fig, ax=plt.subplots()
# plt.ylim(0, 5000)
# plt.xlim(85, 97)
# ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
# ax.plot(null_data, marker='.', label='Null Model', color='C3')
# ax.legend(loc='upper left')
# ax.set_xlabel('Percent of Classes seen')
# ax.set_ylabel('Time (number of steps)')
# #plt.savefig('og_thesis_plot.png', dpi=600)
# plt.show()
#%%
##SPATIAL HETEROGENIETY
sum_diff=abs(np.subtract(la_data, null_data))
sum_diff=np.sum(sum_diff)
sum_diff=sum_diff/100
print("Sum of difference between LA and null:", sum_diff)