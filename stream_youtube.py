# import required libraries
from vidgear.gears import CamGear
import cv2

options = {
    "CAP_PROP_FRAME_WIDTH": 100,
    "CAP_PROP_FRAME_HEIGHT": 100,
    "CAP_PROP_FPS": 10,
}
# Add YouTube Video URL as input source (for e.g https://youtu.be/uCy5OuSQnyA)
# and enable Stream Mode (`stream_mode = True`)
stream = CamGear(
    source="https://www.youtube.com/watch?v=tbYLxz9t5pw",
    stream_mode=True,
    logging=True,
    **options
).start()
# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # Show output window
    cv2.imshow("Output", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()