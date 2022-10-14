# import required libraries
import cv2
from vidgear.gears.stabilizer import Stabilizer
from vidgear.gears import CamGear


options = {"CAP_PROP_FRAME_WIDTH": 720,
           "CAP_PROP_FRAME_HEIGHT": 240,
           "CAP_PROP_FPS": 60}

# assigning it
# To open live video stream on webcam at first index(i.e. 0) device
stream = CamGear(source="test_stab.mp4").start()

# initiate stabilizer object with defined parameters
stab = Stabilizer(smoothing_radius=25, crop_n_zoom=True, border_size=15)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    #frame = cv2.rotate(frame, cv2.ROTATE_180)
    # check for frame if Nonetype
    if frame is None:
        break

    # send current frame to stabilizer for processing
    stabilized_frame = stab.stabilize(frame)
    unstabilized_frame = frame

    # wait for stabilizer which still be initializing
    if stabilized_frame is None:
        continue

    # {do something with the stabilized frame here}

    # Show output window
    cv2.imshow("Output Stabilized Frame", stabilized_frame)
    cv2.imshow("Output UnStab Frame", unstabilized_frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# clear stabilizer resources
stab.clean()

# safely close video stream
stream.stop()
