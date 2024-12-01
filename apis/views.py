from django.shortcuts import render
import pandas as pd
from .models import *
import io
from django.http import HttpResponse

def download_excel(request):
    # Fetch data from the database
    fields = (
        'name', 'age', 'gender', 'address', 'email', 
        'phone', 'courses', 'gpa',)
    
    data = studentsData.objects.all().values(*fields,)

    # Convert to a list of dictionaries 
    data_list = list(data)
    df = pd.DataFrame(data_list)

    # Save dataframe to a BytesIO object
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer: 
        df.to_excel(writer, sheet_name='Students', index=False, header=True)

    output.seek(0)
    
    # Set the HTTP response for downloading the Excel file
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Students_Data.xlsx'
    return response
