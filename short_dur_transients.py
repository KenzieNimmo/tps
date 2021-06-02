"""
Kenzie Nimmo 2021
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import FixedLocator
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

mpl.rcParams['font.size'] = 6
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['legend.fontsize'] = 6
mpl.rcParams['axes.labelsize'] = 6
mpl.rcParams['xtick.labelsize'] = 6
mpl.rcParams['ytick.labelsize'] = 6
mpl.rcParams['xtick.major.pad']='4'
mpl.rcParams['ytick.major.pad']='4'

#* NB. 1 W.Hz^{-1} == 1.05026*10^{-11} Jy.kpc^2    * 
#* --> L = T_B*y**2*(2.761e-23)    Watts/Hz        *      
#*      = [ ]*(1.05025e-13)  Jy,kpc^2              *
# note you need to multiply by 1e9**2 to convert to GHz 

#lines of constant brightness temperature
TB = [1e4,1e8,1e12,1e16,1e20,1e24,1e28,1e32,1e36,1e40,1e44,1e48]
x=np.linspace(1e-10,1e2,100)

for tb in TB:
    plt.plot(x,tb*(x**2)*2.761e-5*1.05025e-13,color='k',lw=0.3,alpha=0.2,linestyle='--')

# add TB labels
plt.text(5e-9,1e11,r'$10^{44}$ K',rotation=30,color='k',alpha=0.3)
plt.text(1.5e-8,1e8,r'$10^{40}$ K',rotation=30,color='k',alpha=0.3)
plt.text(5e-8,1e5,r'$10^{36}$ K',rotation=30,color='k',alpha=0.3)
plt.text(1.5e-7,1e2,r'$10^{32}$ K',rotation=30,color='k',alpha=0.3)
plt.text(5e-7,1e-1,r'$10^{28}$ K',rotation=30,color='k',alpha=0.3)
plt.text(1.5e-6,1e-4,r'$10^{24}$ K',rotation=30,color='k',alpha=0.3)
plt.text(5e-6,1e-7,r'$10^{20}$ K',rotation=30,color='k',alpha=0.3)
plt.text(5e-5,1e-9,r'$10^{16}$ K',rotation=30,color='k',alpha=0.3)
# FRBs non-repeaters (only localised FRBs)

# Pulsars general (psrcat)
psr=open('pulsars.txt','r')
lines=psr.readlines()
psrx=[]
psry=[]
for n in lines:
    psrx.append(float(n.split()[4])) 
    psry.append(float(n.split()[5]))


plt.scatter(psrx,psry,color='pink',marker='x',alpha=0.3)
plt.text(1e-5,1e-5,'Pulsars',color='pink')

# RRATs general
rrat=open('rrats.txt','r')
lines=rrat.readlines()
rratx=[]
rraty=[]
for n in lines:
    rratx.append(float(n.split()[4]))
    rraty.append(float(n.split()[5]))


plt.scatter(rratx,rraty,color='magenta',marker='x',alpha=0.5)
plt.text(1e-1,1e2,'RRATs',color='magenta')

# Crab giant pulses
crabgrp=np.loadtxt('crab_giant.txt')
crabip=np.loadtxt('crab_giant.ip.txt')
crabgrpx=[]
crabgrpy=[]
for n in range(len(crabgrp)):
    crabgrpx.append(crabgrp[n][0]*crabgrp[n][1]*1e-3)
    crabgrpy.append(crabgrp[n][2]/crabgrp[n][1] * (2)**2)

for n in range(len(crabip)):
    crabgrpx.append(crabip[n][0]*crabip[n][1]*1e-3)
    crabgrpy.append(crabip[n][2]/crabip[n][1] * (2)**2)

plt.scatter(crabgrpx,crabgrpy,color='coral',marker='x',alpha=0.01)
plt.text(1e-6,1e0,'Crab GRPs',color='coral')

# Crab nano-shots (Hankins+2003 and Jessner+2010)
cnano=np.loadtxt('crab_nano.txt')
for n in range(len(cnano)):
    plt.scatter(cnano[n][0],cnano[n][1],color='orange',marker='+')
plt.text(5e-9,1e2,'Crab nanoshots',color='orange')

# The other nano-shots

# FRB 121102 range
#spitler+2016, Scholz+2017, law+2017, michilli+2018, hessels+2018, gourdji+2018, gajjar+2018,hardy+2017, Houben+2019, Majid+2020, Josephy+2020, Rajwade+2020, Caleb+2020

# order is freq in GHz, width in ms and Fluence in Jy ms
frb121102=np.loadtxt('frb121102.txt')
frb121102x=[]
frb121102y=[]
for n in range(len(frb121102)):
    frb121102x.append(frb121102[n][0]*frb121102[n][1]*1e-3)
    frb121102y.append(frb121102[n][2]/frb121102[n][1] * (972e3)**2)


plt.scatter(frb121102x,frb121102y,color='lightblue',marker='x',alpha=0.4)
plt.text(1e-1,5e11,'FRB 20121102A',color='lightblue')

# R3 range
# CHIME/FRB discovery paper, Marcote+2020, Chawla+2020, CHIME/FRB periodicity, Pleunis+2021
frb180916=np.loadtxt('frb180916.txt')
frb180916x=[]
frb180916y=[]
for n in range(len(frb180916)):
    frb180916x.append(frb180916[n][0]*frb180916[n][1]*1e-3)
    frb180916y.append(frb180916[n][2]/frb180916[n][1] * (149e3)**2)


plt.scatter(frb180916x,frb180916y,color='blue',marker='x',alpha=0.4)
plt.text(1e-1,5e9,'FRB 20180916B',color='blue')

# SGR 1935+2154 range
sgr = np.loadtxt('sgr1935.txt')
sgrx=[]
sgry=[]
for n in range(len(sgr)):
    sgrx = np.append(sgrx,sgr[n][1])
    sgry = np.append(sgry,sgr[n][0])

plt.scatter(sgrx,sgry,alpha=0.8,color='purple',marker='x')
plt.text(5e-3,1e5,'SGR 1935+2154',color='purple')
#plt.fill_between([np.min(sgrx),np.max(sgrx)],[np.min(sgry),np.min(sgry)],[np.max(sgry),np.max(sgry)],alpha=0.7,color='pink')

# FRB 190711
# Macquart+2020, Kumar+2020
frb190711=np.loadtxt('frb190711.txt')
frb190711x=[]
frb190711y=[]
for n in range(len(frb190711)):
    frb190711x.append(frb190711[n][0]*frb190711[n][1]*1e-3)
    frb190711y.append(frb190711[n][2]/frb190711[n][1] * (2700e3)**2)


plt.scatter(frb190711x,frb190711y,color='green',marker='x',alpha=0.7)
plt.text(1e-1,5e13,'FRB 20190711A',color='green')

# R3 Nimmo et al. 2021
frb180916_micro = np.loadtxt('frb180916_micro.txt')
frb180916_microx=[]
frb180916_microy=[]
for n in range(len(frb180916_micro)):
    frb180916_microx.append(frb180916_micro[n][0]*frb180916_micro[n][1]*1e-3)
    frb180916_microy.append(frb180916_micro[n][2]/frb180916_micro[n][1] * (149e3)**2)


plt.scatter(frb180916_microx,frb180916_microy,color='springgreen',marker='*',alpha=0.7)
plt.text(1e-7,1e13,'FRB 20180916B (Nimmo et al. 2021)', color='springgreen')

# M81R Nimmo et al. 2021b
m81nano=np.loadtxt('m81_nano.txt')
m81nanox = []
m81nanoy = []
for n in range(len(m81nano)):
    m81nanox.append(m81nano[n][0]*m81nano[n][1]*1e-3)
    m81nanoy.append(m81nano[n][2]/m81nano[n][1] * (3.6e3)**2)


plt.scatter(m81nanox,m81nanoy,color='k',marker='*')
plt.text(3e-7,1e7,'FRB 20200120E (this work)', color='black')


plt.xscale('log')
plt.yscale('log')
plt.xlim(1e-9,10)
plt.ylim(1e-10,1e16)


plt.ylabel(r'Spectral Luminosity [erg s$^{-1}$ Hz$^{-1}$]')
plt.xlabel(r'Transient Duration ($\nu\ W$) [GHz s]')

# ticks
plt.axes().tick_params(axis = 'both', which = 'minor', labelsize = 0, labelcolor='white')
plt.axes().set_xticks([1e-8,1e-6,1e-4,1e-2,1], minor=True)
plt.axes().set_yticks([1e-9,1e-8,1e-6,1e-5,1e-3,1e-2,1,10,1e3,1e4,1e6,1e7,1e9,1e10,1e12,1e13,1e15], minor=True)

plt.axes().set_xticks([1e-9,1e-7,1e-5,1e-3,1e-1,10])
plt.axes().set_xticklabels([r'$10^{-9}$',r'$10^{-7}$',r'$10^{-5}$',r'$10^{-3}$',r'$10^{-1}$',r'$10^{1}$'])

plt.axes().set_yticks([1e-10,1e-7,1e-4,1e-1,1e2,1e5,1e8,1e11,1e14])
plt.axes().set_yticklabels([r'$10^{10}$',r'$10^{13}$',r'$10^{16}$',r'$10^{19}$',r'$10^{22}$',r'$10^{25}$',r'$10^{28}$',r'$10^{31}$',r'$10^{34}$'])



plt.savefig('TPS.pdf',format='pdf',dpi=300)
plt.show()
