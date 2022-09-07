

import mysql.connector

mydb = mysql.connector.connect(
                                         host='localhost',
                                         database='RecycleReward',
                                         user='root',
                                         password='FmySql@my123')

products_type = ["plastic", "glass", "paper box", "cans"]

total_item_scaned = 0  
score = 0

mycursor = mydb.cursor()

brc= input("Hello, Please Enter the Barcode:  ")
# my_data=(brc,)
my_data = [brc,]
b = []
q="SELECT * FROM productnew where BARCODE =%s"
try:
  mycursor.execute(q,my_data)
  my_data=mycursor.fetchall()
  for row in my_data:
    print(row) # print the row in list
    print("------")
    print("------")
    # print(row)
    
    # CONVERTING TUPLE INTO LIST
    
    lt = list(row)
    print(lt)
    print("          ")
    print(lt[2])
    
    x = lt[2].lower()
    
    for product in products_type:
        
      total_item_scaned += 1
      if "plastic" == x:
          first = products_type
          score +=25
          print("            ")
          print('Great! you earned 25 points from this product')
          break
      
          
      # total_item_scaned += 1
      if "glass" == x:
          first = products_type
          score +=20
          print('Great! you earned 20 points from this product')
          break
      # total_item_scaned += 1
      if "can" == x:
        first = products_type
        score +=15
        print('Great! you earned 15 points from this product')
        break
        
    # total_item_scaned += 1
      if "paper box" == x:
        first = products_type
        score +=10
        print('Great! you earned 10 points from this product')
        break
      
    else:
      first = None
      print(first)
        
    print(f'\nnumber of items is {total_item_scaned}')
    print(f'your total reward points are {score}')
  
  
    

except Exception as e:
    print(e)

mycursor = mydb.cursor()
