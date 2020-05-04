import hashlib, os
import matplotlib.pyplot as plt
import cv2

def find_duplicates():
    '''
    This function finds the duplicates in an image folder.
    The folder will contain 'n' number of images, from which duplicate images will be removed.
    @param folder_name : name of the folder containing images

    returns (duplicates_name, duplicates)
    '''
    try:
        folder_name = r'test/'
        # set this as current path
        os.chdir(folder_name)
        os.getcwd()
    except:
        print("Image folder '.test/' does not exists !")
        return (0, 0, 0)
    # extract all images 
    all_images = os.listdir()
    # to store duplicates
    duplicates = []
    # to store duplicate names
    duplicates_name = []
    # to store hash values
    hash_keys = dict()
    # find duplicates inside the directory
    for index, filename in  enumerate(os.listdir('.')):  #listdir('.') = current directory
        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                # convert in image hash value
                filehash = hashlib.md5(f.read()).hexdigest()
            # add hash key of an image if not present
            if filehash not in hash_keys:
                hash_keys[filehash] = index
            # if already present, then consider it to be duplicate
            else:
                duplicates.append((index,hash_keys[filehash]))
                duplicates_name.append(filename)
    return duplicates_name, duplicates, all_images

def show_duplicates(duplicates):
    for file_indexes in duplicates[:len(duplicates)]:
        try:
            img_1 = cv2.imread(all_images[file_indexes[1]])
            img_2 = cv2.imread(all_images[file_indexes[0]])
            
            img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB) 
            img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
            
            plt.subplot(121),plt.imshow(img_1)
            plt.title(all_images[file_indexes[1]]), plt.xticks([]), plt.yticks([])

            plt.subplot(122),plt.imshow(img_2)
            plt.title(all_images[file_indexes[0]] + ': DUPLICATE'), plt.xticks([]), plt.yticks([])
            plt.show()
        except OSError as e:
            continue

''' execute '''
# find duplicates
duplicates_name, duplicates, all_images = find_duplicates()
print(f"Duplicates found : {len(duplicates_name)}")
print(duplicates_name)
# show duplicates
show_duplicates(duplicates)