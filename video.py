import cv2
import os

dream_name = 'starry_night'
dream_path = 'dream/{}'.format(dream_name)


fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

out = cv2.VideoWriter('{}.mp4'.format(dream_name),fourcc, 30.0, (1284,589))

for i in range(999999999999999999999999999):
    if os.path.isfile('dream/{}/img_{}.jpg'.format(dream_name,i+1)):
        pass
    else:
        dream_length = i
        break

for i in range(dream_length):
    img_path = os.path.join(dream_path,'img_{}.jpg'.format(i))
    print(img_path)
    frame = cv2.imread(img_path)
    out.write(frame)

out.release()


