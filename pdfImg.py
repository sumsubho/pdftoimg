import fitz  # PyMuPDF "pip install PyMuPDF"
import os
import sys
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
mylist = os.listdir("pdfs")
print("task started")
for idx,f in enumerate(mylist):
    if idx >= n1-1 and idx < n1+n2-1:
        file_name, file_ext = os.path.splitext(f)
        if file_ext == '.pdf':
            isExist = os.path.exists(f"images/{file_name}")
            if not isExist:
                os.makedirs(f"images/{file_name}")
            file_path = "pdfs/"+f
            doc = fitz.open(file_path)  # open document
            for i, page in enumerate(doc):
                pix = page.get_pixmap(dpi=200)  # render page to an image
                pix.save(f"images/{file_name}/{file_name}_page_{i}.png")
            print(f"{idx+1} : {f} completed")
print("task finished")