import hashlib, os

def main():
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
        return (0, 0)
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
    return duplicates_name, duplicates


''' execute '''
duplicates_name, duplicates = main()
print(f"Duplicates found : {len(duplicates_name)}")
print(duplicates_name)