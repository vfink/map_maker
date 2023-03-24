from PyPDF2 import PdfReader

pdf_path = '/Users/victorfink/Documents/Projects/map_maker/Philadelphia Map Final.pdf'
pdf = PdfReader(str(pdf_path))
print(pdf.metadata)
page = pdf.pages[0]
print(len(page.images))

count = 0

for image_file_object in page.images:
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)
        count += 1
        print("COUNT: ",str(count))