import math
import numpy as np
import csv

import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True  # Enable LaTeX rendering


Pi = 3.14159265359 
Log10 = 2.30258509299

fourpi = 4*Pi

limit1 = 10000000

t_init = 1
t_max = 20
bins = 5000
t_step = (t_max - t_init)/bins
t_values = np.linspace(t_init,t_max,bins)


lam_init = 0.5


def one_lp_beta(lam):
	dlam = 3*(lam**2)/(16*Pi**2)
	return dlam

def two_lp_beta(a):
	dlam = 3*(lam**2)/(16*Pi**2) - 5.6666*(lam**3)/((16*Pi**2)**2)
	return dlam


array_lam_1lp = []
array_lam_2lp = []

array_t_1lp = []
array_t_2lp = []






######################
####   ONE LOOP   ####
######################

# Init Value
lam = lam_init

for t in t_values:
	dlam = one_lp_beta(lam)
	lam_temp = lam + t_step*dlam

	if lam_temp > limit1:
		break
	lam = lam_temp

	array_t_1lp.append(t)
	array_lam_1lp.append(lam)



######################
####   TWO LOOP   ####
######################

# Init Value
lam = lam_init

for t in t_values:
	dlam = two_lp_beta(lam)
	lam_temp = lam + t_step*dlam

	if lam_temp > limit1:
		break
	lam = lam_temp

	array_t_2lp.append(t)
	array_lam_2lp.append(lam)


# Writing to CSV file:   EVOLUTION DATA
with open("phi4_theory-data-evolution_1lp_of_lambda_for_init_lam_"+str(lam_init).replace(".","_")+".csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["(0) t", "(1) lambda"])  # Header
    writer.writerows(zip(array_t_1lp, array_lam_1lp))  # Writing data

##        TWO LOOP


# Writing to CSV file:   EVOLUTION DATA
with open("phi4_theory-data-evolution_2lp_of_lambda_for_init_lam_"+str(lam_init).replace(".","_")+".csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["(0) t", "(1) lambda"])  # Header
    writer.writerows(zip(array_t_2lp, array_lam_2lp))  # Writing data


print("CSV files created successfully")

######################################
#######    PLOTTING        ###########
######################################



fig, ax = plt.subplots(figsize=(9, 8))



ax.plot(array_t_1lp, array_lam_1lp, linewidth = 2.5, linestyle="dotted", color='r', label=r'1-loop')
ax.plot(array_t_2lp, array_lam_2lp, linewidth = 2.5, linestyle="solid", color='b', label=r'2-loop')

if lam_init > 3.0:
	plt.ylim((-0.005,150))

plt.xlim((1,20))



# plt.axhline(y = 0, color = 'b', linewidth = 1.7, linestyle = 'dotted')
# plt.axhline(y = 4*Pi, color = 'k', linewidth = 1.7, linestyle = 'dotted', label=r'$4 \pi$')

plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.xlabel(r'$\log\mu$',fontsize=24)
plt.ylabel(r'$\lambda$',fontsize=24)
# plt.title(r'Evolution of $a$ for ODD loop order',fontsize=24)
text_content = r'$\mu_0 =$'+" "+str(10)+"\n "+r'$\lambda(\mu_0) = $'+" "+str(lam_init)
plt.legend(fontsize=15)

bbox_props = dict(boxstyle="round, pad=0.3", facecolor="floralwhite", edgecolor="black", linewidth=1)
ax.text(0.46, 0.78, text_content, transform=ax.transAxes,  ha="center", va="center", fontsize=20, bbox=bbox_props)

ax.margins(x=0, y = None) 

# plt.savefig("phi4_evol_1lp_2lp_lam_lambda_init_"+str(lam_init).replace(".","_")+".png", dpi=250, bbox_inches='tight')

plt.savefig("phi4_theory-plot-evolution_1lp_of_lambda_for_init_lam_"+str(lam_init).replace(".","_")+".png", dpi=250, bbox_inches='tight')
plt.savefig("figure2a.png", dpi=250, bbox_inches='tight')
plt.show()