# pdftoimg

Step 1 : Need to install python 
Step 2 : open cmd and run the command "pip install PyMuPDF"
step 3 : place your pdf files in the pdfs folder
step 4 : open the cmd in the root folder and run the following command
python pdfimg.py <position of the file> <number of files>

as an example if you want to start converting from the 5th file and total 100 files , the command will be 

python pdfimg.py 5 100

if you do not have 100 files , the execuation will stop once it reaches to the final file.

the images will be stored inside images folder under the subfolder with the name of the pdf files.

