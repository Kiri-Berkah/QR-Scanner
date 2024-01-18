import cv2
import requests

cap = cv2.VideoCapture(1)
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    
    if data:
        amount = 4000
        # Fleet ID is different based on every bus
        fleet_id = "d1d9be6c-fa0d-425a-a224-e3986715bad3" 
        user_id = data.strip('/') 
        api_url = f"https://hfbe-x7qbuf5z4q-et.a.run.app/api/v1/qr/{user_id}/{fleet_id}/{amount}"

        response = requests.post(api_url)

        print("Response Code:", response.status_code)
        print("Response Content:", response.text)

        break

    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
