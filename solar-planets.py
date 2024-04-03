import cv2

img = cv2.imread("solar-system.jpg")

planet_texts = [
    ("Mercury", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Venus", (150, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Earth", (250, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Mars", (350, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Jupiter", (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Saturn", (550, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Uranus", (650, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Neptune", (750, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
]

for planet_text in planet_texts:
    text, position, font, font_scale, color, thickness = planet_text
    cv2.putText(img, text, position, font, font_scale, color, thickness)

cv2.imshow("output", img)

cv2.waitKey(0)

cv2.imwrite("Solar_system_with_name.jpg", img)

cv2.destroyAllWindows()
