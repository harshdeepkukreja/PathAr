# import matplotlib.pyplot as plt
# from netCDF4 import Dataset
# import numpy as np
# from mpl_toolkits.basemap import Basemap

# file = 'mean_air_surface_temp.nc' # relative humidity data
# data = Dataset(file, mode='r') # read the data 
# print(type(data)) # print the type of the data 
# print(data.variables.keys()) # print the variables in the dat

# lats = data.variables['lat'][:]  
# longs = data.variables['lon'][:]
# time = data.variables['mrdtime'][:]
# air_temp = data.variables['T2MMEAN'][:]

# mp = Basemap(projection='merc',
#              llcrnrlon= -180,   # lower longitude
#              llcrnrlat= -78,    # lower latitude
#              urcrnrlon=180,   # uppper longitude
#              urcrnrlat = 85,   # uppper latitude
#             resolution ='i')

# a = int(input("Enter day for which you want to visualize Air Surface Temp: "))
# lon, lat = np.meshgrid(longs,lats)  #this converts coordinates into 2D arrray
# x,y = mp(lon,lat) #mapping them together 
# plt.figure(figsize=(10,10)) #figure size 
# c_scheme = mp.pcolor(x,y,np.squeeze(air_temp[a,:,:]),cmap = 'jet') # [0,:,:] is for the first day of the year

# # consider this as the outline for the map that is to be created 
# mp.drawcoastlines()
# mp.drawstates()
# mp.drawcountries()

# cbar = mp.colorbar(c_scheme,location='right',pad = '10%') # map information
# plt.title('Average Air Surface Temp. for Day ' + str(a) + ' of year 2022')
# plt.show()

# plt.savefig('air_temp.jpg',dpi=300) #saves the image generated


# lon, lat = np.meshgrid(longs,lats)
# x,y = mp(lon,lat)
# plt.figure(figsize=(12,12)) #figure size 

# # loop for all the days 
# days = np.arange(0,31)  # for considering all days of the year

# for i in days:
#     c_scheme = mp.pcolor(x,y,np.squeeze(air_temp[i,:,:]),cmap = 'jet')
#     mp.drawcoastlines()
#     mp.drawstates()
#     mp.drawcountries()

#     cbar = mp.colorbar(c_scheme,location='right',pad = '10%')
#     day = i+1

#     plt.title('Average Air Surface Temp. for the Day ' + str(day) +  ' of year 2022')
#     plt.clim(-60,40)
    
#     plt.savefig(r'D:\college work\cllg smester 5\NASA Hackathon\data\air_surface_temp'+ '\\' + str(day)+'.jpg')
#     plt.clf()

#     import PIL

# image_frames = [] # creating a empty list to be appended later on
# days = np.arange(1,31)

# for k in days:
#     new_fram = PIL.Image.open(r'D:\college work\cllg smester 5\NASA Hackathon\data\air_surface_temp' + '\\' + str(k) + '.jpg') 
#     image_frames.append(new_fram)

# image_frames[0].save('air_temp_timelapse.gif',format='GIF',
#                     append_images = image_frames[1: ],
#                     save_all = True, duration = 500,
#                     loop = 0)

# import xarray as xr
# import os

# nc_file = 'mean_air_surface_temp.nc'
# csv_file = open('air_surface_temp.csv', 'w', newline='')
# ds = xr.open_dataset(nc_file)
# df = ds.to_dataframe()
# df.to_csv(csv_file)

# mean_air_temp_by_lon = data.groupby(['lon'])['T2MMEAN'].mean().reset_index()
# print(mean_air_temp_by_lon.head(4))
# mean_air_temp_by_lon.plot(x="lon", y=["T2MMEAN"],kind="line", figsize=(20,20))
# plt.show()

# mean_air_temp_by_lat = data.groupby(['lat'])['T2MMEAN'].mean().reset_index()
# mean_air_temp_by_lat.plot(x="lat", y=["T2MMEAN"],kind="line", figsize=(20,20))
# plt.show()

# mean_rhum_by_time = data.groupby(['mrdtime'])['T2MMEAN'].mean().reset_index()
# mean_rhum_by_time.plot(x="mrdtime", y=["T2MMEAN"],kind="line", figsize=(20,20))
# plt.show()

print("Samarth")