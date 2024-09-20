 import json
    #open the file
    with open('student.json') as f:
    data = json.load(f)
    #print the data
    print(data)
    #print each student data
    for student in data['students']:
         print('ID:', student['id'])
         print('Name:', student['name'])
         print('Age:', student['age'])
         print('Grades:', student['grades'])
            print() 

