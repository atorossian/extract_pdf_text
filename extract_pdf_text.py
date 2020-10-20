# Importo librerías
import PyPDF2, os, re,pyperclip,sys

# Formato de la ruta
# Formato genérico C:\Das_fda s8\f-d+s áfdA66sf\fds 43afaÉ\
path=False
path_regex=re.compile(r'''
(                                   # Grupo 1: Ruta entera
([a-zA-Z]\:)                        # Grupo 2: Carpeta Raíz
((\\[a-zA-Z0-9áéíóúÁÉÍÓÚ\-+_\s]+)+) # Grupo 3: Carpetas con separador
(\\)                                # Grupo 4: Separador final
)
''',re.VERBOSE)

# Especificar ruta del archivo
while path==False:
    try:
        path_name=str(input('Enter a path to the file you want to work with: '))
        check_path_name=path_regex.match(path_name)
        path_name_checked=check_path_name[0]
        os.chdir(path_name_checked)
        path=True
        print('The path you entered is correct!')
    except:
        if path_name=='quit':
            break
        print(path_name + ' is not a valid path.\nEnter a valid path to continue.\nPaths usually have this format: "root:\folder1\folder2\folder3\".')
    if path_name=='quit':
        sys.exit

# Formato del nombre del archivo
# Formato genérico: frasvfaÁ0045432DSEéág
file=False
file_regex=re.compile(r'[a-zA-Z0-9áéíóúÁÉÍÓÚ_\-+\s]+(\.pdf)')

# Especificar nombre del archivo
while file==False:
    try:
        file_name=input('Enter the name of the file you want to work with: ')
        check_file_name=file_regex.match(file_name)
        file_name_checked=check_file_name[0]
        file=True
        print('The file you entered is correct!')
    except:
        if file_name=='quit':
            break
        print(file_name + ' is not a valid file name.\nCheck if the file you want to work with is in the specified folder, you entered the file extension or that name of the file was not modified')
    if file_name=='quit':
        sys.exit    

# Verificar qué desea hacer el usuario
y_n=str(input('Do you want to extract the text from the specified file(y/n)? '))
if y_n=='y':
    print('Processing file...\nPlease wait.')
    try:
        # Crear archivo de texto
        output_file=open(file_name_checked+'.txt','a')
        # Levantar archivo PDF
        pdf_file=open(file_name_checked,'rb')
        # Leer archivo PDF
        reader=PyPDF2.PdfFileReader(pdf_file)
        # Extraer texto
        for page_num in range(reader.numPages):
            page=reader.getPage(page_num).extractText()
            # Pegar en archivo de texto
            output_file.write(page)
        output_file.close()
        y_n2=str(input('The text was extracted successfully!\nThe file was saved on the specified path.\nDo you want to access the file content (y/n)? '))
        if y_n2=='y':
            for page_num in range(reader.numPages):
                print(reader.getPage(page_num).extractText())
        else:
            sys.exit
        y_n3=str(input('Do you want to close the application(y/n)? '))
        if y_n3=='y':
            print('Closing application.')
        else:
            
    except:
        print('An error has occured!\nThe application could not extract the text from the specified file.')
else:
    print('Closing application.')
    sys.exit

