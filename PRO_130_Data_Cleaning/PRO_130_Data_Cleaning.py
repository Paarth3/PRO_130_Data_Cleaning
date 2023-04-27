import csv
import pandas as pd

old_names = []
old_dists = []
old_masses = []
old_radii = []
new_masses = []
new_radii = []
headers = ['Names', 'Distance', 'Mass', 'Radius']
data_1 = []
data_2 = []

# Open Brown Dwarf file
df = pd.read_csv("D:/WhiteHat_Jr/WhiteHat_Jr_Python/PROJECTS/PRO_128_Web_Scrapping_2/Field_brown_dwarfs.csv", encoding='Windows-1252')
data_list = df.values.tolist()
for row in data_list:
    old_names.append(row[0])
    old_dists.append(row[1])
    old_masses.append(row[2])
    old_radii.append(row[3])

# Remove 'nan' values
for index, old_name in enumerate(old_names):
    if str(old_name) == 'nan':
        old_names[index] = ''

for index, old_dist in enumerate(old_dists):
    if str(old_dist) == 'nan':
        old_dists[index] = ''

for index, old_mass in enumerate(old_masses):
    if str(old_mass) == 'nan':
        old_masses[index] = ''

for index, old_radius in enumerate(old_radii):
    if str(old_radius) == 'nan':
        old_radii[index] = ''

# Convert Mass and radius into float type
for index, old_mass in enumerate(old_masses):
    try:
        old_masses[index] = float(old_masses[index])
    except:
        old_masses[index] = ''

for index, old_radius in enumerate(old_radii):
    try:
        old_radii[index] = float(old_radii[index])
    except:
        old_radii[index] = ''

# Multiply radius by 0.102763
for old_radius in old_radii:
    try:
        new_radii.append(float(old_radius)*0.102963)
    except:
        new_radii.append('')

# Multiply mass by 0.000954588
for old_mass in old_masses:
    try:
        new_masses.append(float(old_mass)*0.000954588)
    except:
        new_masses.append('')

# Save into a new CSV File
with open('New_Field_brown_dwarfs.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    for i in range(len(data_list)):
        csv_writer.writerow([old_names[i], old_dists[i], new_masses[i], new_radii[i]])

#TODO Merge with brightest start file
with open("D:/WhiteHat_Jr/WhiteHat_Jr_Python/PROJECTS/PRO_127_Web_Scrapping_1/Star_data.csv", 'r') as f:
    csv_reader = csv.reader(f)
    data_1 = list(csv_reader)

with open("D:/WhiteHat_Jr/WhiteHat_Jr_Python/PROJECTS/PRO_129_Data_Merging/New_Field_brown_dwarfs.csv", 'r') as f:
    csv_reader = csv.reader(f)
    data_2 = list(csv_reader)

with open('Merged_data.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(data_1[0])
    csv_writer.writerows(data_1[1:])
    csv_writer.writerows(data_2[1:])