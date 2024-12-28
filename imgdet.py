##install openCV before running this code.
import cv2
def detface(imagepath):
    image = cv2.imread(imagepath)
    if image is None:
        print("Error: Could not load image.")
        return
    facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if facecascade.empty():
        print("Error: Could not load Haar Cascade for face detection.")
        return
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(grayimage, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) == 0:
        print("No faces detected.")
    else:
        print(f"Detected {len(faces)} face(s).")
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
imagepath = 'image.jpg'
detface(imagepath)

