import glob
from fpdf import FPDF
import sys
import os

if __name__ == '__main__':
    input_dir = sys.argv[1]
    os.chdir(input_dir)
    pdf = FPDF()
    a = glob.glob("*/*.jpg")
    a = sorted(a)

    for image in a:
        pdf.add_page()
        pdf.image(image,0,0,210,297)
    
    saved_name = "{}.pdf".format(input_dir)
    print(saved_name)
    pdf.output(saved_name, "F")
