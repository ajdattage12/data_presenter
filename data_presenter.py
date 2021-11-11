open_file = open("CupcakeInvoices.csv")
# print(open_file)

for line in open_file:
    print(line)


for line in open_file:
    line = line.strip()
    values = line.split(',')
    print(values[2])


for line in open_file:
    line = line.strip()
    values = line.split(',')
    
    quanity = float(values[3])
    price = float(values[4])
    total_price = quanity * price
    print(total_price)
total_invoice = 0 


for line in open_file:
    line = line.strip()
    values = line.split(',')

    quanity = float(values[3])
    price = float(values[4])
    total_invoice += quanity * price
print(total_invoice)


open_file.close()