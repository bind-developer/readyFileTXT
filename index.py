#with open("data.txt") as archivo:
#    print(archivo.readline())

#with open("data1.txt","r") as archivo:
 #   linea_trama=archivo.read().split("||||")
 #   print(linea_trama)

rows = 1
num_change = 1
# Abrimos el archivo en modo lectura.
# encoding='utf-8'
text_out = open('LE2060041427620231100130100001111_out.txt', 'w')
with open("LE2060041427620231100130100001111.TXT","r",errors='ignore') as file:

    # Iteramos el archivo abierto con readline()
    print(file)
    for line in file:
        strline=line.rstrip()
        line_split = strline.split("|")
        if line_split[13] in ('02','03'):
            if len(line_split[12])==9:
                print(rows, 'CUO: ' + line_split[1], '|', 'NUM CORRELATIVO: ' + line_split[12])
                strnum_correlativo=line_split[12]
                intnum_correlativo=int(strnum_correlativo)
                strline=strline.replace(strnum_correlativo, str(intnum_correlativo))
                print(rows,strline)
                num_change +=1
        text_out.write(strline + '\n')
        rows += 1
    text_out.close()
    print("COUNT ROWS UPDATE: ",num_change)
