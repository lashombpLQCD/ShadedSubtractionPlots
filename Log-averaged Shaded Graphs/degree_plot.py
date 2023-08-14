
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

data4444 = scipy.io.loadmat('re_expo_rel_var_poly_4444.mat') 
re_expo_rel_var_poly_4444 = np.transpose(data4444['re_expo_rel_var_poly_4444'])
re_expo_rel_var_poly_4444 = re_expo_rel_var_poly_4444[0]
bottom_4444 = np.transpose(data4444['bottom_poly_4444'])
bottom_4444 = bottom_4444[0]
top_4444 = np.transpose(data4444['top_poly_4444'])
top_4444 = top_4444[0]
dppoly4444 = data4444['dppoly4444'] 
dppoly4444 = dppoly4444[0]


# Loading 8888 

data8888 = scipy.io.loadmat('re_expo_rel_var_poly_8888.mat') 
re_expo_rel_var_poly_8888 = np.transpose(data8888['re_expo_rel_var_poly_8888'])
re_expo_rel_var_poly_8888 = re_expo_rel_var_poly_8888[0]
bottom_8888 = np.transpose(data8888['bottom_poly_8888'])
bottom_8888 = bottom_8888[0]
top_8888 = np.transpose(data8888['top_poly_8888'])
top_8888 = top_8888[0]
dppoly8888 = data8888['dppoly8888'] 
dppoly8888 = dppoly8888[0]

# Loading 12121216

data12121216 = scipy.io.loadmat('re_expo_rel_var_poly_12121216.mat') 
re_expo_rel_var_poly_12121216 = np.transpose(data12121216['re_expo_rel_var_poly_12121216'])
re_expo_rel_var_poly_12121216 = re_expo_rel_var_poly_12121216[0]
bottom_12121216 = np.transpose(data12121216['bottom_poly_12121216'])
bottom_12121216 = bottom_12121216[0]
top_12121216 = np.transpose(data12121216['top_poly_12121216'])
top_12121216 = top_12121216[0]
dppoly12121216 = data12121216['dppoly12121216'] 
dppoly12121216 = dppoly12121216[0]

# Loading 24242432

data24242432 = scipy.io.loadmat('re_expo_rel_var_poly_24242432.mat') 
re_expo_rel_var_poly_24242432 = np.transpose(data24242432['re_expo_rel_var_poly_24242432'])
re_expo_rel_var_poly_24242432 = re_expo_rel_var_poly_24242432[0]
bottom_24242432 = np.transpose(data24242432['bottom_poly_24242432'])
bottom_24242432 = bottom_24242432[0]
top_24242432 = np.transpose(data24242432['top_poly_24242432'])
top_24242432 = top_24242432[0]
dppoly24242432 = data24242432['dppoly24242432'] 
dppoly24242432 = dppoly24242432[0]


# Defining colors for plots in hex (to match Matlab)  

# c[0] = cyan, c[1] = magenta, c[2] = green, c[3] = red, c[4] = black 
c = ['#00ffff', '#ff00ff', '#00ff00', '#ff0000', '#000000']


# Plotting Log-log plots of data 

plt.semilogy(dppoly4444, re_expo_rel_var_poly_4444, '-', label = "POLY $4^3 \\times 4$", color = c[0])
plt.fill_between(dppoly4444, re_expo_rel_var_poly_4444 - bottom_4444, re_expo_rel_var_poly_4444 + top_4444, color=c[0], alpha=0.3)

plt.semilogy(dppoly8888, re_expo_rel_var_poly_8888, '-', label = "POLY $8^3 \\times 8$", color = c[1])
plt.fill_between(dppoly8888, re_expo_rel_var_poly_8888 - bottom_8888, re_expo_rel_var_poly_8888 + top_8888, color=c[1], alpha=0.3)

plt.semilogy(dppoly12121216, re_expo_rel_var_poly_12121216, '-', label = "POLY $12^3 \\times 16$", color = c[2])
plt.fill_between(dppoly12121216, re_expo_rel_var_poly_12121216 - bottom_12121216, re_expo_rel_var_poly_12121216 + top_12121216, color=c[2], alpha=0.3)

plt.semilogy(dppoly24242432, re_expo_rel_var_poly_24242432, '-', label = "POLY $24^3 \\times 32$", color = c[3])
plt.fill_between(dppoly24242432, re_expo_rel_var_poly_24242432 - bottom_24242432, re_expo_rel_var_poly_24242432 + top_24242432, color=c[3], alpha=0.3)


# Option to change the legend border to black 

legend = plt.legend(fontsize="9") 
sb = legend.get_frame() 
sb.set_edgecolor('black')


# Defining axis labels and set limits

plt.xlabel('$\it{Polynomial}$ $\it{Degree}$', fontname='Segoe UI') 
plt.ylabel('$\it{Log-averaged}$ $\it{Relative}$  $\it{Variance}$', fontname='Segoe UI')  
plt.ylim(1.0*10**(-2), 1.0*10**(0))
plt.xlim(0, 1000)

# Remove default seaborn border around figure 
#sns.despine() 


# Change seaborn dpi settings for saving higher dpi images 
sns.set(rc={"figure.dpi":600, 'savefig.dpi':600}) 


# Show plots 
plt.show() 




