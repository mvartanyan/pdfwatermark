from io import BytesIO
from re import match

import click
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from webcolors import hex_to_rgb


@click.command()
@click.argument('filename')
@click.option('-w', '--watermark', default='TEST',
              help='Annotation text, use {} to include parts of file name if '
                   'you are using --regex')
@click.option('-r', '--regex', default='',
              help='Regex to run on file name, annotation is used as template')
@click.option('-f', '--font-name', default='Helvetica-Bold',
              help='Font name')
@click.option('-s', '--font-size', default=85, type=int,
              help='Font size')
@click.option('-c', '--color', default='#000000',
              help='Font colour')
@click.option('-o', '--opacity', default=1.0,
              help='Opacity from 0 (transparent) to 1 (solid)')
@click.option('-x', default=250,
              help='X coordinate')
@click.option('-y', default=250,
              help='Y coordinate')
@click.option('-d', '--destination-file-name', default='',
              help='Destination file, by default files are modified in place')
def annotate(filename, watermark, regex, font_name, font_size, color, opacity,
             x, y, destination_file_name):
    mask_stream = BytesIO()

    watermark_canvas = canvas.Canvas(mask_stream, pagesize=A4)
    watermark_canvas.setFont(font_name, font_size)
    r, g, b = hex_to_rgb(color)
    c = Color(r, g, b, alpha=opacity)
    watermark_canvas.setFillColor(c)

    if regex:
        groups = match(regex, filename)
        watermark = watermark.format(*groups.groups())

    watermark_canvas.drawString(x, y, watermark)
    watermark_canvas.save()

    mask_stream.seek(0)

    mask = PdfReader(mask_stream)
    src = PdfReader(filename)
    output = PdfWriter()

    for page_num in range(len(src.pages)):
        page = src.pages[page_num]
        page.merge_page(mask.pages[0])
        output.add_page(page)

    if not destination_file_name:
        destination_file_name = filename

    with open(destination_file_name, "wb") as output_stream:
        output.write(output_stream)


if __name__ == '__main__':
    annotate()
