
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.io 


'''
    A Python script for plotting the relative variance for POLY versus the 
    GMRES relative residual norm for the lattices 4^4, 8^4, and 12^3 x 16

    -PL 
'''



# Loading 4444

data4444 = scipy.io.loadmat('rel_poly4444_gmres.mat') 
rel_poly4444 = np.transpose(data4444['rel_poly4444'])
rel_poly4444 = rel_poly4444[0]
rel_poly4444_errbars = np.transpose(data4444['rel_poly4444_errbars'])
rel_poly4444_errbars = rel_poly4444_errbars[0]
rntolpoly4444 = data4444['rntolpoly4444'] 
rntolpoly4444 = rntolpoly4444[0]


# Loading 8888 

data8888 = scipy.io.loadmat('rel_poly8888_gmres.mat') 
rel_poly8888 = np.transpose(data8888['rel_poly8888'])
rel_poly8888 = rel_poly8888[0]
rel_poly8888_errbars = np.transpose(data8888['rel_poly8888_errbars'])
rel_poly8888_errbars = rel_poly8888_errbars[0]
rntolpoly8888 = data8888['rntolpoly8888'] 
rntolpoly8888 = rntolpoly8888[0]

# Loading 12121216

data12121216 = scipy.io.loadmat('rel_poly12121216_gmres.mat') 
rel_poly12121216 = np.transpose(data12121216['rel_poly12121216'])
rel_poly12121216 = rel_poly12121216[0]
rel_poly12121216_errbars = np.transpose(data12121216['rel_poly12121216_errbars'])
rel_poly12121216_errbars = rel_poly12121216_errbars[0]
rntolpoly12121216 = data12121216['rntolpoly12121216'] 
rntolpoly12121216 = rntolpoly12121216[0]


# Defining colors for plots in hex (to match Matlab)  

# c[0] = cyan, c[1] = magenta, c[2] = green, c[3] = red, c[4] = black 
c = ['#00ffff', '#ff00ff', '#00ff00', '#ff0000', '#000000']


# Plotting Log-log plots of data 

plt.loglog(rntolpoly4444, rel_poly4444, '-', label = "POLY $4^3 \\times 4$", color = c[0])
plt.fill_between(rntolpoly4444, rel_poly4444 - rel_poly4444_errbars, rel_poly4444 + rel_poly4444_errbars, color=c[0], alpha=0.3)

plt.loglog(rntolpoly8888, rel_poly8888, '-', label = "POLY $8^3 \\times 8$", color = c[1])
plt.fill_between(rntolpoly8888, rel_poly8888 - rel_poly8888_errbars, rel_poly8888 + rel_poly8888_errbars, color=c[1], alpha=0.3)

plt.loglog(rntolpoly12121216, rel_poly12121216, '-', label = "POLY $12^3 \\times 16$", color = c[2])
plt.fill_between(rntolpoly12121216, rel_poly12121216 - rel_poly12121216_errbars, rel_poly12121216 + rel_poly12121216_errbars, color=c[2], alpha=0.3)


# Option to change the legend border to black 

legend = plt.legend() 
sb = legend.get_frame() 
sb.set_edgecolor('black')


# Inverting x-axis so smaller residual norms further to right (Only necessary when plotting GMRES residual norm) 
plt.gca().invert_xaxis() 


# Defining axis labels and set limits

plt.xlabel('$\it{GMRES}$ $\it{Relative}$ $\it{Residual}$ $\it{Norm}$', fontname='Segoe UI') 
plt.ylabel('$\it{Relative}$  $\it{Variance}$', fontname='Segoe UI')  
plt.ylim(1.0*10**(-6), 1.0*10**(0))
plt.xlim(1.0*10**(0), 1.0*10**(-6))


# Remove default seaborn border around figure 
#sns.despine() 


# Change seaborn dpi settings for saving higher dpi images 
sns.set(rc={"figure.dpi":600, 'savefig.dpi':600}) 


# Show plots 
plt.show() 




