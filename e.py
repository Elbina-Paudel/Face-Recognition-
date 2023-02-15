for i in range(5):
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
       
        check, frame = webcam.read()

        cv2.imshow("Capturing", frame)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
  
        key = cv2.waitKey(1)

        if key == ord('s') : 
            face_locations = face_recognition.face_locations(rgb_small_frame)
            if face_locations != []:
                face_encoding = face_recognition.face_encodings(frame)[0]
                if ref_id in embed_dictt:
                    embed_dictt[ref_id]+=[face_encoding]
                else:
                    embed_dictt[ref_id]=[face_encoding]
                webcam.release()
                cv2.waitKey(1)
                cv2.destroyAllWindows()     
                break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
