from read import read_file
from datetime import datetime

def rent_equipment():
    print("Thank you for buying")
    print("\n")
    print("*********************************************************************")
    print("We will need your name and number to print bill")
    print("*********************************************************************")
    print("\n")
    name = input("Enter your name :")
    phone = input("Enter your phone :")
    print("*******************************************************************************************************")
    print("S.N. \t Nme \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
    print("*******************************************************************************************************")
    a = 1
    file = open("Laptop.txt","r")
    for line in file:
        print(a, "\t" + line.replace(",","\t"))
        a =a+ 1
    print("*******************************************************************************************************")  
    file.close()
    print("\n")
    
    valid_id = int(input("Please Provide the ID of the product you want to buy:"))
    print("\n")

    #Valid ID

    while valid_id <= 0 or valid_id > len(read_file()):
        print("Please provide a valid Laptop ID !!")
        print("\n")
        valid_id = int(input("Please Provide the ID of the laptop you want to buy:"))
    user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to buy:"))
    print("\n")

    #Valid Quantity

    my_dict = read_file()
    get_quantity = my_dict[valid_id][3]
    while user_quantity <= 0 or user_quantity > int(get_quantity):
        print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the Laptop screen")
        print("\n")
        user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to buy: "))
    print("\n")

    #Update the text file

    my_dict[valid_id][3] = int(my_dict[valid_id][3]) + int(user_quantity)

    file = open("Laptop.txt","w")

    for values in my_dict.values():
        file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
        file.write("\n")
    file.close()

    #Purchasing from manufacturer

    
    product_name = my_dict[valid_id][0]
    quantity_of_user = user_quantity
    price_of_unit = my_dict[valid_id][2]
    price_of_item = my_dict[valid_id][2].replace("$",'')
    final_price = int(price_of_item)*int(quantity_of_user)

    rent_equipment = []
    rent_equipment.append([product_name, quantity_of_user, price_of_item, final_price])

    
    total = 0
    VAT = 0.13*(final_price)
    for i in rent_equipment:
        total += int(i[3])
    final_total = final_price + VAT
    date_time = datetime.now()
    print("\n")
    print("\t \t \t \t Azam's Laptop Shop")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9864949649 ")
    print("\n")
    print("****************************************************************************************")
    print("Laptop Details: ")
    print("****************************************************************************************")
    print("Customer Name:" + str(name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("****************************************************************************************")
    print("\n")
    print("Purchase Details are:")
    print("************************************************************************************************************")
    print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
    print("************************************************************************************************************")
    for i in rent_equipment:
        print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
    print("************************************************************************************************************")
    
    print("Vat Amount:",  VAT)
    print("Grand Total:" + str(final_total))
    print("Note: Vat Amount added to grand total")

    return name,phone,date_time,rent_equipment,VAT,final_total
    

    # today_date_and_time = datetime.now()
    
    with open(str(name) + str(phone) +".txt", "w")as file:
        file.write("\n")
        file.write("\t \t \t \t Azam's Laptop Shop")
        file.write("\n")
        file.write("\t \t Kamalpokhari, Kathmandu | Phone No: 9864949649 ")
        file.write("\n")
        file.write("****************************************************************************************\n")
        file.write("Laptop Details: ")
        file.write("\n")
        file.write("*******************\n")
        file.write("Customer Name:" + str(name))
        file.write("\n")
        file.write("Phone Number: " + str(phone))
        file.write("\n")
        file.write("Date and Time: " + str(date_time))
        file.write("\n")
        file.write("****************************************************************************************\n")
        file.write("\n")
        file.write("Purchase Details are:")
        file.write("\n")
        file.write("***************************************************************************************************\n")
        file.write("Product Name \t\t Total Quantity \t\t Unit Price \t\t Total")
        file.write("\n")
        file.write("***************************************************************************************************\n")
        for i in rent_equipment:
            file.write(str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t" + str(i[2]) + "\t\t\t" + "$" + str(i[3])+"\n")
        file.write("***************************************************************************************************\n")
        file.write("\n")
        if VAT:
            file.write("Vat Amount:" +""+ str(VAT)+ "\n")
            file.write("\n")
            file.write("Grand Total: $" + str(final_total)+ "\n")
            file.write("\n")
            file.write("Note: Vat Amount added to grand total" + "\n")
            file.write("\n")
        else:
            file.write("Grand Total: $" + str(final_total))
          




def sale_laptop():
    print("Thank you for selling")
    print("\n")
    print("*********************************************************************")
    print("We will need your name and number to print bill")
    print("*********************************************************************")
    print("\n")
    name = input("Enter your name :")
    phone = input("Enter your phone :")
    print("*********************************************************************************************************")
    print("S.N. \t Name \t\t      Brand \t   Price \t Quantity \t Processor \t Graphic Card")
    print("*********************************************************************************************************")
    a = 1
    file = open("Laptop.txt","r")
    for line in file:
        print(a, "\t" + line.replace(",","\t"))
        a =a+ 1
    print("*********************************************************************************************************")  
    file.close()
    print("\n")
    
    valid_id = int(input("Please Provide the ID of the product you want to sell:"))
    print("\n")

    #Valid ID

    while valid_id <= 0 or valid_id > len(read_file()):
        print("Please provide a valid Laptop ID !!")
        print("\n")
        valid_id = int(input("Please Provide the ID of the laptop you want to sell:"))
    user_quantity = int(input("Please Provide the number of quantity of the laptop you want to sell:"))
    print("\n")

    #Valid Quantity

    my_dict = read_file()
    get_quantity = my_dict[valid_id][3]
    while user_quantity <= 0 or user_quantity > int(get_quantity):
        print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the Laptop screen")
        print("\n")
        user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to sell: "))
    print("\n")

    #Update the text file

    my_dict[valid_id][3] = int(my_dict[valid_id][3]) - int(user_quantity)

    file = open("Laptop.txt","w")

    for values in my_dict.values():
        file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
        file.write("\n")
    file.close()

    #getting user purchased items....................................................

    product_name = my_dict[valid_id][0]
    quantity_of_user = user_quantity
    price_of_unit = my_dict[valid_id][2]
    price_of_item = my_dict[valid_id][2].replace("$",'')
    final_price = int(price_of_item)*int(quantity_of_user)

    rent_equipment = []
    rent_equipment.append([product_name, quantity_of_user, price_of_item, final_price])
    date_time = datetime.now()
    cost_of_shipping = input("Dear Customer do you want your laptop to be shipped?(Y/N)")

    print("\n")
    print("\t \t \t \t  Azam's Laptop Shop")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9864949649 ")
    print("****************************************************************************************")
    print("\n")
    print("Laptop Details: ")
    print("*****************")
    print("Customer Name:" + str(name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("****************************************************************************************")
    print("\n")
    print("Purchase Details are:")
    print("************************************************************************************************************")
    print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
    print("************************************************************************************************************")
    for i in rent_equipment:
        print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
    print("************************************************************************************************************")

    if cost_of_shipping == "Y":
        total = 0
        cost_of_shipping = 500
        for i in rent_equipment:
            total += int(i[3])
        final_total = final_price + cost_of_shipping
        print("Shipping Cost:", cost_of_shipping)
        print("Grand Total:" + str(final_total))
        print("Note: Shipping Cost added to grand total")
        
    else:
        print("Grand Total: $" + str(final_total))

        
        
        total = 0
        cost_of_shipping = 0
        for i in rent_equipment:
            total += int(i[3])
        final_total = final_price + cost_of_shipping
        date_time = datetime.now()
        print("\n")
        print("\t \t \t \t Azam's Laptop Shop")
        print("\n")
        print("\t \t Kamalpokhari, Kathmandu | Phone No: 9864949649 ")
        print("****************************************************************************************")
        print("Laptop Details: ")
        print("******************")
        print("Customer Name:" + str(name))
        print("Phone Number: " + str(phone))
        print("Date and Time: " + str(date_time))
        print("****************************************************************************************")
        print("\n")
        print("Purchase Details are:")
        print("***************************************************************************************************")
        print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
        print("***************************************************************************************************")
        for i in rent_equipment:
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
        print("***************************************************************************************************")
        if cost_of_shipping:
            print("Shipping Cost:", cost_of_shipping)
            print("Grand Total:" + str(final_total))
            print("Note: Shipping Cost added to grand total")
        else:
            print("Grand Total: $" + str(final_total))
        
    return name,phone,date_time,rent_equipment,cost_of_shipping,final_total
