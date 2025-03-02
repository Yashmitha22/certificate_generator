import cv2
import os
from fpdf import FPDF

TEMPLATE_PATH = r"C:\Users\yashm\Downloads\certificate\sample.jpg"
OUTPUT_DIR = "generate_certificate"
os.makedirs(OUTPUT_DIR, exist_ok=True)
participants = [
    
    {"name": "abc", "college": "xyz"},
]

def generate_certificate(name, college):
    template = cv2.imread(TEMPLATE_PATH)
    if template is None:
        print("Error: Certificate template will not be found!")
        return None
    name_position = (600, 548)   
    college_position = (39, 616)

    cv2.putText(template, name, name_position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    max_length = 100  
    if len(college) > max_length:
        words = college.split()
        mid = len(words) // 2
        first_line = " ".join(words[:mid])
        second_line = " ".join(words[mid:])
        cv2.putText(template, first_line, college_position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(template, second_line, (college_position[0], college_position[1] ), 
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(template, college, college_position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    
    img_path = os.path.join(OUTPUT_DIR, f"{name}.jpg")
    cv2.imwrite(img_path, template)
    
    
    pdf_path = os.path.join(OUTPUT_DIR, f"{name}.pdf")
    pdf = FPDF(orientation="L", unit="mm", format="A4")  
    pdf.add_page()
    pdf.image(img_path, x=0, y=0, w=297, h=210)  
    pdf.output(pdf_path)

    print(f"✅ Certificate generated for {name} in PDF landscape format")
    return pdf_path

for participant in participants:
    generate_certificate(participant["name"], participant["college"])

print("🎉 All certificates generated successfully in **proper PDF landscape format**!")
