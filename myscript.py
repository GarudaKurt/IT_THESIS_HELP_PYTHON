import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

isFirebase_initialized = False

def initialize_firebase():
    global isFirebase_initialized
    if not isFirebase_initialized:
        cred = credentials.Certificate('C:\\workspace\\IT_THESIS_ARDUINO\\python\\arduino-741ed-firebase-adminsdk-2mxkq-4a92967ef6.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://arduino-741ed-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
        isFirebase_initialized = True

def main():
    initialize_firebase()
    try:
        myserial = serial.Serial('COM5', 9600)
        print('Serial port opened successfully.')
        while True:
            if myserial.in_waiting > 0:
                data = myserial.readline().strip()
                barcodeID = int(data)
                sendData = {
                    'barcode': {
                        'barcodeID': barcodeID,
                    }
                }
                db.reference('barcode').update(sendData['barcode'])
                print('Value of barcode id {}'.format(barcodeID))
    except Exception as e:
        print(f"Error something wrong: {e}")

if __name__ == "__main__":
    main()
