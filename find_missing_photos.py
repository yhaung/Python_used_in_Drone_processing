import arcpy,os
maindir ='C:\\Users\\Lenovo\\Desktop\\TGO_Mission\\'
def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:
                file = file.lower()
                if file.startswith("d"):
                    if file.endswith(".jpg"):
                        r.append(file)# inserting the previous data
                        print (file)

    return r
myfiles =list_files(maindir)
file = open("C:\\Users\\Lenovo\\Desktop\\TGO_Missionphoto_list_GeoTag.txt","w")
for x in myfiles:
    file.write(x+"\n")