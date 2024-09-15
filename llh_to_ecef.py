# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km ...
#   converts LLH components to ECEF

# Parameters:
#   lat_deg: latitude in deg
#   lon_deg: longitude in deg
#   hae_km: height above ellipsoid in km

# Output:
#   ECEF vector components in km
#
# Written by Grant Chapman
# Other contributors: None

# import Python modules
import math # math module
import sys # argv

# constants
R_E_KM = 6378.137
E_E    = 0.081819221456

## calculate demoninator
# (eccentricity, latitude in radians)
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-ecc**2.0 * math.sin(lat_rad)**2.0)

# initialize script arguments
lat_deg = float('nan')
lon_deg = float('nan')
hae_km  = float('nan')

# parse script arguments
if len(sys.argv) == 4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km  = float(sys.argv[3])
else:
  print(\
    'Usage: '\
    'python3 ecef_to_llh.py r_x_km r_y_km r_z_km'\
  )
  exit()

### script below this line ###

# initialize lat_rad
lat_rad = lat_deg*math.pi/180.0
lon_rad = lon_deg*math.pi/180.0
c_E = R_E_KM / calc_denom(E_E, lat_rad)
s_E = R_E_KM*(1-E_E**2) / calc_denom(E_E, lat_rad)

# finding ECEF components
r_x_km = (c_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (c_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (s_E+hae_km)*math.sin(lat_rad)

# print
print('r_x = ',r_x_km,' km')
print('r_y = ',r_y_km,' km')
print('r_z = ',r_z_km,' km')
