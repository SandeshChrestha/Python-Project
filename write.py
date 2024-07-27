 # today_date_and_time = datetime.now()
def write_sold(name,phone,date_time,rent_equipment,cost_of_deliverd,final_total):
    with open(str(name) + str(phone) +".txt", "w")as file:
        file.write("\n")
        file.write("\t \t \t \tSandeh shop")
        file.write("\n")
        file.write("\t \t Banepa Chardobato | Phone No: 01149978 ")
        file.write("\n")
        file.write("****************************************************************************************\n")
        file.write("\n")
        file.write("Equipment Details: ")
        file.write("\n")
        file.write("******************\n")
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
        if cost_of_deliverd == 200:
            file.write("Delivery Cost:" +""+ str(cost_of_deliverd)+ "\n")
            file.write("\n")
            file.write("Grand Total: $" + str(final_total)+ "\n")
            file.write("\n")
            file.write("Note: Shipping Cost added to grand total" + "\n")
        else:
            file.write("Grand Total: $" + str(final_total))







def write_purchase(name,phone,date_time,rent_equipment,final_total):
    with open(str(name) + str(phone) +".txt", "w")as file:
        file.write("\n")
        file.write("\t \t \t \t Sandesh Shop")
        file.write("\n")
        file.write("\t \tBanepa, Chardobato | Phone No: 01149978 ")
        file.write("\n")
        file.write("****************************************************************************************\n")
        file.write("Equipment Details: ")
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
            file.write("Grand Total: $" + str(final_total))
        else:
            file.write("Grand Total: $" + str(final_total))
        
