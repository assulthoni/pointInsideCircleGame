import cv2
import numpy as np


def generate_random_point():
    x, y = np.random.randint(512), np.random.randint(512)
    return x, y


def is_inside_circle_area(x_true, y_true, rad, x, y):
    if (x - x_true) * (x - x_true) + (y - y_true) * (y - y_true) <= rad * rad:
        return True
    else:
        return False


def click_event(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_PLAIN
        color = (0, 255, 0) if is_inside_circle_area(x_true, y_true, 50, x, y) else (0, 0, 255)
        status = "Correct" if is_inside_circle_area(x_true, y_true, 50, x, y) else "Wrong"
        if not is_inside_circle_area(x_true, y_true, 50, x, y):
            xtocenter = x - x_true
            ytocenter = y - y_true
            quadratic = np.square(xtocenter) + np.square(ytocenter)
            distance = np.sqrt(quadratic) - 50
            statusDistance = f"distance to circle: {distance}"
        else:
            statusDistance = 0
        stringAll = f"{status} : {statusDistance}"
        print(stringAll)
        cv2.putText(background, status, (x, y), font, 1, color, 2)
        cv2.imshow("Main Window", background)


if __name__ == '__main__':
    background = np.zeros((512, 512, 3), np.uint8)
    x_true, y_true = generate_random_point()
    cv2.circle(background, (x_true, y_true), 50, (0, 0, 0))
    print(x_true, y_true)
    cv2.imshow("Main Window", background)
    cv2.setMouseCallback("Main Window", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
