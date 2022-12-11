import csv
from datetime import *
#define inventory class

"""
An inventory class to manaage electronics store data
Provides various output files based on the input
"""
class Inventory:
    
    def __init__(self,manufactureData,priceData,serviceData):
        
        self.manufactureData=manufactureData
        self.priceData=priceData
        self.serviceData=serviceData
    #string representantion
    def __str__(self):
        return "Inventory class"
    
    #define function to load data
    def loadData(self):
        global manufacture,price,service
        manufacture = []
        price = []
        service = []

        
        with open(self.manufactureData) as file:
            data= csv.reader(file)
            for line in data:
                manufacture.append(line)
                
            #for debugging
            print(manufacture)
        with open(self.priceData) as file:
            
            data= csv.reader(file)
            for line in data:
                price.append(line)
                
            #for debugging
            print(price)
        with open(self.serviceData) as file:
            data= csv.reader(file)
            for line in data:
                service.append(line)
                
            #for debugging
            print(service)
    def idsorter(self,list):
        return list[0]
    
    def alphasorter(self,list):
        return list[1]
        
    def sortDataId(self):
        global manufactureSorted,priceSorted,serviceSorted
        manufactureSorted= sorted(manufacture,key=self.idsorter)
        priceSorted=sorted(price,key=self.idsorter)
        serviceSorted=sorted(service,key=self.idsorter)
        
        # print('sorted')
        # print(manufactureSorted)
        # print(priceSorted)
        # print(serviceSorted)
    #appending the prices and service dates to the main list
    def appendData(self):
        for x in range(0, len(manufactureSorted)):
            manufactureSorted[x].append(priceSorted[x][1])

        for x in range(0, len(manufactureSorted)):
            manufactureSorted[x].append(serviceSorted[x][1])
            
        # print('all')   
        # print(manufactureSorted)
    def sortDataAlpha(self):
        global allSorted 
        allSorted=sorted(manufactureSorted,key=self.alphasorter)
        print('all') 
        print(allSorted)
    # lookign in each list for specific item types damaged and past service and appending them to their own lists
    def itemTypes(self):
        
        global tower_list,laptop_list,phone_list,item_type
        item_type = allSorted
        tower_list = []
        laptop_list = []
        phone_list = []
        
        
        
        for x in range(0, len(item_type)):
            if item_type[x][2] == "tower":
                tower_list.append(item_type[x])
            elif item_type[x][2] == "phone":
                phone_list.append(item_type[x])
            elif item_type[x][2] == "laptop":
                laptop_list.append(item_type[x])
    #method to sort item types based on id          
    def sortItems(self):
        global sortedtower_list,sortedlaptop_list,sortedphone_list
        sortedtower_list=sorted(tower_list,key=self.idsorter)
        sortedlaptop_list=sorted(tower_list,key=self.idsorter)
        sortedphone_list=sorted(tower_list,key=self.idsorter)
        
    #method to generate past service list    
    def pastServiceInventory(self):
        global pastServiceList
        pastServiceList=[]
        today= datetime.now()
        for x in range(0,len(item_type)):
            itemDate=datetime.strptime(item_type[x][5],'%m/%d/%Y')
            if itemDate < today:
                pastServiceList.append(item_type[x])
                
    def pastServiceSorter(self,list):
        
        return list[5]
    def sortPastService(self):
        global sortedpastServiceList
        sortedpastServiceList=sorted(pastServiceList,key=self.pastServiceSorter,reverse=True)
        
     #Metod to generate damed list              
    def damagedList(self): 
        global damagedlist 
        damagedlist = []
        
        for x in range(0, len(item_type)):
            if item_type[x][3] == "damaged":
                damagedlist.append(item_type[x])  
                    
    def damagedListSorter(self,list):
        return list[4]
    def sortDamagedList(self):
        global sorteddamagedlist
        sorteddamagedlist=sorted(damagedlist,key=self.damagedListSorter)
               
    #Method to create files for diffrent data               
    def writeFiles(self):
        #writefiles for fullinventory
        with open('FullInventory.csv', 'w') as newfile:
            fullInventorywrite = csv.writer(newfile)

            for x in range(0, len(allSorted)):
                fullInventorywrite.writerow(allSorted[x])
        # Writing a file for each item type
        with open('LaptopInventory.csv', 'w') as newfile:
            laptopInventorywrite = csv.writer(newfile)

            for x in range(0, len(sortedlaptop_list)):
                laptopInventorywrite.writerow(sortedlaptop_list[x])

        with open('PhoneInventory.csv', 'w') as newfile:
            phoneInventorywrite = csv.writer(newfile)

            for x in range(0, len(sortedphone_list)):
                phoneInventorywrite.writerow(sortedphone_list[x])

        with open('TowerInventory.csv', 'w') as newfile:
            towerInventorywrite = csv.writer(newfile)

            for x in range(0, len(sortedtower_list)):
                towerInventorywrite.writerow(sortedtower_list[x])
        with open('DamagedInventory.csv', 'w') as newfile:
            damagedInventorywrite = csv.writer(newfile)

            for x in range(0, len(sorteddamagedlist)):
                damagedInventorywrite.writerow(sorteddamagedlist[x])
        with open('PastServiceInventory.csv','w') as newfile:
            pastservice=csv.writer(newfile)
            
            for x in range(0, len(sortedpastServiceList)):
                pastservice.writerow(sortedpastServiceList[x])
print('\nClass instance being initialized ')  
print('\nIgnore the output on the command as they have been used for debugging')    
#create an instance of the inventory class               
inventory=Inventory('ManufacturerList.csv','PriceList.csv','ServiceDatesList.csv')
#call method to load data
inventory.loadData()
#call method to sort data based on id
inventory.sortDataId()
#call method to append the price and past service
inventory.appendData()
inventory.sortDataAlpha()
inventory.itemTypes()
inventory.sortItems()
inventory.damagedList()
inventory.sortDamagedList()
inventory.pastServiceInventory()
inventory.sortPastService()
inventory.writeFiles()
print('\n Invetory process finished .Several Ouputs have been produced for the parent folder .')