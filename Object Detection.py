import cv2


def detect_blobs(filename, output_filename):
    image = cv2.imread(filename)
    if image is None:
        print(f"{filename} couldn't be opened")
        return 


    parameters = cv2.SimpleBlobDetector_Params()

    """Distinguish the blobs from the rest of the image based on their size"""
    parameters.filterByArea = True
    parameters.minArea = 20
    parameters.maxArea = 10000

    """Distinguish the blobs as polka dots using their shape (a circle!)"""
    parameters.filterByCircularity = True
    parameters.minCircularity = 0.6

    parameters.filterByColor = False

    Detector = cv2.SimpleBlobDetector_create(parameters)

    keypoints = Detector.detect(image)

    print(f"{filename} was detected, it has {len(keypoints)} blobs")

    result = cv2.drawKeypoints(image, keypoints, None, (0, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

                               
    cv2.imwrite(output_filename, result)

    print(f"The result has been saved to {output_filename}")

detect_blobs( "/Users/suhaanshaik/Desktop/polka_dots_1.png", "/Users/suhaanshaik/Desktop/polka_dots_1_detected.png")

detect_blobs("/Users/suhaanshaik/Desktop/polka_dots_2.jpg", "/Users/suhaanshaik/Desktop/polka_dots_2_detected.jpg")

detect_blobs( "/Users/suhaanshaik/Desktop/polka_dots_3.jpg", "/Users/suhaanshaik/Desktop/polka_dots_3_detected.jpg")





