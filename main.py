from operation import rent_equipment
from operation import sale_laptop
from write import write_purchase, write_sold

    


print("\n")
print("\n")
print("-------------------------------------------------------------------------------")
print("--------------------------|  Sandesh Rent Shop   |-----------------------------")
print("-------------------------------------------------------------------------------")
print("\t\t  Banepa, chardobato | Telephone:011400110")
print("-------------------------------------------------------------------------------")
print("\n")


continueLoop = True
while continueLoop == True:
    print("\n")
    print("Please choose only one option")
    print("(1) || Press 1 to Rent a Equipments.")
    print("(2) || Press 2 to Return a Equipments.")
    print("(3) || Press 3 to Exit.")
    print("\n")
    print("---------------------------------------------------------------------------")
    userinput = int(input("Choose available option :"))

    if userinput == 1:
            name,phone,date_time,purchased_equipment,final_total = rent_equipment()
            write_purchase(name,phone,date_time,rent_equipment,final_total)

                      
    elif userinput == 2:
            name,phone,date_time,purchased_equipment,cost_of_deliverd,final_total = sale_laptop()
            write_sold(name,phone,date_time,purchased_equipment,cost_of_deliverd,final_total)

        
    elif userinput == 3:
        continueLoop = False
        print("Thank you for Visiting")
    else:
        print("Enter correct option")
