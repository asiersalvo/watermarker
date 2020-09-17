import PyPDF2
import sys

# with open('example/dummy.pdf','rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)

#También podemos hacer:
# with open('example/dummy.pdf','rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.getPage(0))

# with open('example/dummy.pdf','rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf','wb') as new_file:
#         writer.write(new_file)

#PRIMERA FORMA PARA UNIR TODOS LOS PDF'S EN UNO, UNIENDO TODAS LAS PÁGINAS UNA A UNA:
# writer = PyPDF2.PdfFileWriter()
# for i in range(1,len(sys.argv)):
#     reader = PyPDF2.PdfFileReader(sys.argv[i])
#     for x in range(reader.getNumPages()):
#         writer.addPage(reader.getPage(x))
#
# with open('new_pdf.pdf','wb') as new_file:
#     writer.write(new_file)
#SEGUNDA OPCIÓN, UNIR LOS PDF'S ENTEROS UNO DETRAS DE OTRO, AQUÍ CON FUNCIÓN:
# inputs = sys.argv[1:]
# def pdf_combiner (pdf_lists):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_lists:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('new_pdf2.pdf')
#
# pdf_combiner(inputs)

#EJERCICIO WATERMARK PARA PONER UNA MARCA DE AGUA SOBRE PDF'S:
input = sys.argv[1]
output = sys.argv[2]
water = sys.argv[3]
def watermark_pdf (input_pdf, output_pdf, watermarkpdf):
    watermark_obj = PyPDF2.PdfFileReader(watermarkpdf)
    watermark_page = watermark_obj.getPage(0)
    pdf_reader = PyPDF2.PdfFileReader(input_pdf)
    pdf_writer = PyPDF2.PdfFileWriter()
    for i in range(pdf_reader.getNumPages()):
        i = pdf_reader.getPage(i)
        i.mergePage(watermark_page)
        pdf_writer.addPage(i)
    with open(output_pdf,'wb') as new_file:
        pdf_writer.write(new_file)

watermark_pdf(input, output, water)







