import cv2

def resizeImage(image, height=200):
	if(image.shape[0] > height):
		print('Original Dimensions : ', image.shape)
		ratio = image.shape[1]/image.shape[0]
		width = int(height * ratio)
		resized = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)
		print('Resized Dimensions : ', resized.shape)
		return resized
	print("Resize not required")
	return image
