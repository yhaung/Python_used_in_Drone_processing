#export as csv - gps reference from Ebee photo - label,x,y,z,accuracy,yaw,pitch,roll will be extracted
# written by Kyaw Naing Win - OneMap GIS Program Manager, 17 Jan 2019
try:
	import PhotoScan as m
except:
	print ("Photoscan module not exit..")
else:
	import Metashape as m

doc = m.app.document
cur_chunk = doc.chunk
cameras = cur_chunk.cameras
print ("C:\\temp\\reference information....being exported")
csv_name = "C:\\temp\\eBee_photo_reference.csv"
f = open(csv_name,"w+")
for camera in cameras:
	exif= dict(camera.photo.meta)
	pic = camera.label
	x = exif['Exif/GPSLongitude']
	y = exif['Exif/GPSLatitude']
	z = exif['Exif/GPSAltitude']
	gpsXYacc = exif['Sensefly/GPSXYAccuracy' ]
	gpsZacc = exif['Sensefly/GPSZAccuracy']
	pitch = exif['Sensefly/Pitch']
	roll = exif['Sensefly/Roll']
	yaw = exif['Sensefly/Yaw']
	string = pic+","+str(x)+","+str(y)+","+str(z)+","+str(gpsXYacc)+","+str(gpsXYacc)+","+str(gpsZacc)+","+str(yaw)+","+str(pitch)+","+str(roll)+"\n"
	#Label,X/Longitude,Y/Latitude,Z/Altitude,Accuracy_X/Y_(m),Accuracy_Z_(m),Yaw,Pitch,Roll,
	f.write(string)
f.close(),
print ("C:\\temp\\eBee_photo_reference.csv ....export process completed")

cur_chunk.loadReference(csv_name, format = Metashape.ReferenceFormatCSV, columns ='nxyzXYZabc', delimiter =',')
print ("reference informatin loading completed...")