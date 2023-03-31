import subprocess

def convert_pdf_to_html(input_file, output_file):
    try:
        subprocess.check_call(["gs", "-dNOPAUSE", "-dBATCH", "-sDEVICE=html", "-dFirstPage=1", "-dLastPage=1", f"-sOutputFile={output_file}", input_file])
    except subprocess.CalledProcessError as e:
        print("Error converting to HTML:", e)

input_file = "path/to/your/file.pdf"
output_file = "path/to/your/output.html"

convert_pdf_to_html(input_file, output_file)
