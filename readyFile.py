from datetime import datetime

datetime_str = '15/10/2023'
fecha_Variable = datetime.strptime(datetime_str, '%d/%m/%Y')

num_change = 1
text_out = open('LE2049302061820230900130100001111_consig.txt', 'w')
with open("LE2049302061820230900130100001111_out.txt","r",errors='ignore') as file:

    for line in file:
        strline=line.rstrip()
        line_split = strline.split("|")
        if line_split[13] in ('03','04'):
            #fecha_emision = datetime.strptime(line_split[9], '%d/%m/%Y')
            #if fecha_Variable < fecha_emision:
            text_out.write(strline + '\n')
            print(line_split[9])
            num_change += 1
    text_out.close()
    print("COUNT ROWS UPDATE: ", num_change)

# COUNT ROWS UPDATE:  546 in ('01','04','05'):

