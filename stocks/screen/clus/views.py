from django.shortcuts import render
import csv
import openpyxl


def upload_file(request):
    file_content = None

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_name = uploaded_file.name
        file_ext = file_name.split('.')[-1].lower()
        file_content = uploaded_file.read()

        if file_ext == 'csv':
            decoded_file_content = file_content.decode('utf-8').splitlines()
            csv_reader = csv.reader(decoded_file_content)
            file_content = list(csv_reader)

        elif file_ext in ['xlsx', 'xlsm', 'xltx', 'xltm']:
            workbook = openpyxl.load_workbook(filename=uploaded_file)
            sheet = workbook.active
            file_content = []
            for row in sheet.iter_rows(values_only=True):
                file_content.append(row)

    return render(request, 'index2.html', {'file_content': file_content})