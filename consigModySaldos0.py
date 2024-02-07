#---------------------------------------
#seteamos los saldos de consignacio a 0
#--------------------------------------

rows = 1
num_change = 1
# Abrimos el archivo en modo lectura.
# encoding='utf-8'

text_out = open('LE2049302061820231000130100001111_out.txt', 'w')
with open("LE2049302061820231000130100001111.txt", "r", errors='ignore') as file:
    # Iteramos el archivo abierto con readline()
    print(file)
    for line in file:
        strline = line.rstrip()
        line_split = strline.split("|")
        if line_split[13] in ('03', '04'):
            print("orgin", strline)
            line_split[23] = "0.00"
            line_split[24] = "0.00"
            line_split[25] = "0.00"
            print("new","|".join(line_split))
            num_change += 1
        text_out.write("|".join(line_split) + '\n')
        rows += 1
    text_out.close()
    print("Number of rows changed in the column 23,24,25: ", num_change)
    print("Number of rows covered: ", rows)
