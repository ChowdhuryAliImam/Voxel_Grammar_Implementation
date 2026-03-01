import rhinoscriptsyntax as rs
import itertools
import random
import os
import csv
# ==== Setup: rule sequences for each iteration ====


# === File paths ===
mass_rule_path = r"F:\1_CS_440\Project\mass_rules.csv"
court_rule_path = r"F:\1_CS_440\Project\court_rules.csv"

# === Reading CSVs into list of lists ===
rule_list_set = []
court_rule_list_set = []

# Read mass rules
with open(mass_rule_path, 'r') as mfile:
    reader = csv.reader(mfile)
    next(reader)  # skip header
    for row in reader:
        rule_list = [int(val) for val in row[1:] if val.strip() != '']
        rule_list_set.append(rule_list)

# Read court rules
with open(court_rule_path, 'r') as cfile:
    reader = csv.reader(cfile)
    next(reader)  # skip header
    for row in reader:
        rule_list = [val.strip() for val in row[1:] if val.strip() != '']
        court_rule_list_set.append(rule_list)

# ==== Export Paths ====
img_folder = r"F:\1_CS_440\Project\images"
file_folder = r"F:\1_CS_440\Project\files"


# ==== Start iteration over sequences ====
for iteration_index, (rule_list, court_rule_list) in enumerate(zip(rule_list_set, court_rule_list_set)):

    # Clean up Rhino before starting
    rs.DeleteObjects(rs.AllObjects())

    # Initial voxel setup
    initial_shape = rs.AddBox([(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)])
    voxel_length = 1
    voxels = []

    def voxel_array(location, x, y, z):
        for i in range(location[0], x, voxel_length):
            for j in range(location[1], y, voxel_length):
                for k in range(location[2], z, voxel_length):
                    voxel_coord = (i, j, k)
                    voxel = rs.CopyObject(initial_shape, voxel_coord)
                    voxels.append(voxel)

    voxel_array((0, 0, 0), 3, 3, 1)

    point_A = (0, 0, 0)
    vector_1 = rs.VectorCreate(point_A, point_A)
    base_mass = rs.CopyObjects(voxels, vector_1)

    x = y = z = 0
    position = (x, y, z)

    mass_list = []
    mass_Delete = []

    # === Loop through one rule sequence ===
    for rule, court_rule in itertools.izip_longest(rule_list, court_rule_list):

        # === (insert your full original logic here) ===
        # For example: 

        if (rule, court_rule) == (1, 'A'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2])
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2])
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2])
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2])
                
            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass 
            rs.AddLayer(name = 'Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer')
             
            #Deleting voxels from the mass to form court
            #mass_Copy_To_Delete is copying the mass. From this copied mass, the voxels will be deleted.
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer')
            mass_Delete[0:9] = mass_Copy_To_Delete

            #rule-A has no courtyards. therefore no deletition of voxels. bu, need to copy the mass
            
            
        elif (rule, court_rule) == (1, 'B'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2])
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2])
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2])
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2])
                
            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass 
            rs.AddLayer(name = 'Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer')
             
            #Deleting voxels from the mass to form court
            #mass_Copy_To_Delete is copying the mass. From this copied mass, the voxels will be deleted.
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])
            rs.DeleteObject(mass_Delete[5])
            rs.DeleteObject(mass_Delete[7])
            rs.DeleteObject(mass_Delete[8])
            
            
        elif (rule, court_rule) == (1, 'C'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2])
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2])
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2])
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2])
                
            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass 
            rs.AddLayer(name = 'Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer')
             
            #Deleting voxels from the mass to form court
            #mass_Copy_To_Delete is copying the mass. From this copied mass, the voxels will be deleted.
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[1])
            rs.DeleteObject(mass_Delete[4])
            
        elif (rule, court_rule) == (1, 'D'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2])
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2])
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2])
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2])
                
            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass 
            rs.AddLayer(name = 'Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer')
             
            #Deleting voxels from the mass to form court
            #mass_Copy_To_Delete is copying the mass. From this copied mass, the voxels will be deleted.
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])


        elif (rule, court_rule) == (2, 'A'):

            #randomness for copying mass in each of the 4 sides

            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer1')
            
            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer1')
            mass_Delete[0:9] = mass_Copy_To_Delete
            

        elif (rule, court_rule) == (2, 'B'):

            #randomness for copying mass in each of the 4 sides

            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer1')
            
            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer1')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])
            rs.DeleteObject(mass_Delete[5])
            rs.DeleteObject(mass_Delete[7])
            rs.DeleteObject(mass_Delete[8])

        elif (rule, court_rule) == (2, 'C'):

            #randomness for copying mass in each of the 4 sides

            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer1')
            
            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer1')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[1])
            rs.DeleteObject(mass_Delete[4])
            

        elif (rule, court_rule) == (2, 'D'):

            #randomness for copying mass in each of the 4 sides

            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer1')
            
            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer1')
            rs.DeleteObject(mass_Delete[4])

        elif (rule, court_rule) == (3, 'A'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-1, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+1, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-1, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer2')

            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete =rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer2')
            mass_Delete[0:9] = mass_Copy_To_Delete
           
            
            
        elif (rule, court_rule) == (3, 'B'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-1, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+1, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-1, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer2')

            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete =rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer2')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])
            rs.DeleteObject(mass_Delete[5])
            rs.DeleteObject(mass_Delete[7])
            rs.DeleteObject(mass_Delete[8])
            

        elif (rule, court_rule) == (3, 'C'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-1, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+1, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-1, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer2')

            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete =rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer2')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[1])
            rs.DeleteObject(mass_Delete[4])

        elif (rule, court_rule) == (3, 'D'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-1, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+1, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-1, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer2')

            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete =rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer2')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])

        elif (rule, court_rule) == (4, 'A'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1]+1, position [2])
            elif random_number == 2:
                point_A = (position[0]-1, position[1]+1, position [2])
            elif random_number == 3:
                point_A = (position[0]-1, position[1]-1, position [2])
            elif random_number == 4:
                point_A = (position[0]+1, position[1]-1, position [2])

            #copying the mass

            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer3')
            
            #Deleting voxels from the mass to form court
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete , layer='Del_Layer3')
            mass_Delete[0:9] = mass_Copy_To_Delete
            
            
        elif (rule, court_rule) == (4, 'B'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1]+1, position [2])
            elif random_number == 2:
                point_A = (position[0]-1, position[1]+1, position [2])
            elif random_number == 3:
                point_A = (position[0]-1, position[1]-1, position [2])
            elif random_number == 4:
                point_A = (position[0]+1, position[1]-1, position [2])

            #copying the mass

            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer3')
            
            #Deleting voxels from the mass to form court
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete , layer='Del_Layer3')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])
            rs.DeleteObject(mass_Delete[5])
            rs.DeleteObject(mass_Delete[7])
            rs.DeleteObject(mass_Delete[8])
            
            
        elif (rule, court_rule) == (4, 'C'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1]+1, position [2])
            elif random_number == 2:
                point_A = (position[0]-1, position[1]+1, position [2])
            elif random_number == 3:
                point_A = (position[0]-1, position[1]-1, position [2])
            elif random_number == 4:
                point_A = (position[0]+1, position[1]-1, position [2])

            #copying the mass

            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer3')
            
            #Deleting voxels from the mass to form court
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete , layer='Del_Layer3')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[1])
            rs.DeleteObject(mass_Delete[4])


        elif (rule, court_rule) == (4, 'D'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (1,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1]+1, position [2])
            elif random_number == 2:
                point_A = (position[0]-1, position[1]+1, position [2])
            elif random_number == 3:
                point_A = (position[0]-1, position[1]-1, position [2])
            elif random_number == 4:
                point_A = (position[0]+1, position[1]-1, position [2])

            #copying the mass

            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer3')
            
            #Deleting voxels from the mass to form court
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete , layer='Del_Layer3')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])

        #updating the location the location for copying objects after each iteration

        bbox = rs.BoundingBox(mass_list[0])
        if bbox:
            corner = bbox[0]  # same as first grip point
            x = int(corner[0])
            y = int(corner[1])
            z = int(corner[2])
            position = (x, y, z)
        else:
            print("Warning: Bounding box not found. Position unchanged.")

        #updating the mass to be copied
        base_mass = mass_list[0:9]

    # === After each sequence is complete: Save image and model ===
    index_str = str(iteration_index).zfill(4)
    img_path = os.path.join(img_folder, "{}.jpg".format(index_str))
    file_path = os.path.join(file_folder, "{}.3dm".format(index_str))

    rs.Command('_-ViewCaptureToFile "{}" Width=1920 Height=1080 Scale=1 TransparentBackground=No Enter'.format(img_path), echo=False)
    rs.Command('_-SaveAs "{}" Enter'.format(file_path), echo=False)


