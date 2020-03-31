from tkinter import *
from tkinter.ttk import Progressbar
import mysql.connector

#establishing connection to local database
mydatabase = mysql.connector.connect(host="localhost", user="root", passwd=" ", database= "EricAffyStore")

mycursor = mydatabase.cursor()

# mycursor.execute("Show tables")

# for i in mycursor:
	# print(i)
# print(mycursor)


##Creating insert options
def add_new_customer(): 
	print("Enter customer first name")
	Customer_Fname = input()
	print(Customer_Fname)
	print("Enter customer middle name")
	Customer_MInit = input()
	print(Customer_MInit)
	print("Enter customer last name")
	Customer_LName = input()
	print(Customer_Lname)
	print("Enter customer street address")
	Customer_Street = input()
	print(Customer_Street)
	print("Enter customer city of residence")
	Customer_City = input()
	print(Customer_City)
	print("Enter customer current state of residence (e.g.ON)")
	Customer_State = input()
	print(Customer_State)
	print("Enter customer postal address")
	Customer_Postal = input()
	print(Customer_Postal)
	print("Enter customer email address")
	Customer_Email = input()
	print(Customer_Email)

	print("INSERT INTO Customer VALUES (NULL, Customer_Fname, Customer_MInit,Customer_LName, Customer_Street, Customer_City, Customer_State, Customer_Postal, Customer_Email)")
	mycursor.execute("INSERT INTO Customer VALUES (NULL, Customer_Fname, Customer_MInit,Customer_LName, Customer_Street, Customer_City, Customer_State, Customer_Postal, Customer_Email)")

	mydatabase.commit()

	print("Enter value '1' to proceed to purchase transaction details")
	choice = input()
	if(choice == "1"):
		add_new_transaction_details()
	else:
		return

	mydatabase.commit()


def add_new_supplier(): 
	print("Enter supplier's  name")
	Supplier_Name = input()
	print(Supplier_Name)
	print("Enter supplier's street")
	Supplier_Street = input()
	print(Supplier_Street)
	print("Enter supplier's city")
	Supplier_City = input()
	print(Supplier_City)
	print("Enter supplier's state (e.g.ON)")
	Supplier_State = input()
	print(Supplier_State)
	print("Enter supplier's postal code")
	Supplier_Postal = input()
	print(Supplier_Postal)
	print("INSERT INTO Supplier VALUES (NULL, Supplier_Name, Supplier_Street, Supplier_City, Supplier_State, Supplier_Postal)")
	mycursor.execute("INSERT INTO Supplier VALUES (NULL, Supplier_Name, Supplier_Street, Supplier_City, Supplier_State, Supplier_Postal)")
	
	mydatabase.commit()
	 # choice = input()
	print("Enter value '1' to proceed to product order transaction details ")
	choice = input()
	if(choice == "1"):
		add_purchase_information()
	else:
		return

	mydatabase.commit()

def add_new_transaction_details(): 
	order_ID = int(time.time())
	print("Enter order date (YY-MM-DD)")
	Order_Date = input()
	print(Order_Date)
	print("Enter order quantity")
	Order_Quantity = input()
	print(Order_Quantity)
	print("Enter product ID")
	Enter_productID = input()
	print(Enter_productID)
	print("Customer ID")
	Customer_ID = input()
	print(Customer_ID)
	print("Enter total amount of purchase")
	Total_amount = input()
	print(Total_amount)

	print("INSERT INTO Order_Transaction VALUES (Order_ID, Order_Date, Order_Quantity, Product_ID, Customer_ID, Total_Payment)")
	mycursor.execute("INSERT INTO Order_Transaction VALUES (Order_ID, Order_Date, Order_Quantity, Product_ID, Customer_ID, Total_Payment)")
	print("UPDATE Inventory SET InStock_Quantity = InStock_Quantity - (Select Order_Quantity FROM Order_Transaction) WHERE Inventory.Product_ID = Order_Transaction.Product_ID")
	mycursor.execute("UPDATE Inventory SET InStock_Quantity = InStock_Quantity - (Select Order_Quantity FROM Order_Transaction) WHERE Inventory.Product_ID = Order_Transaction.Product_ID")
	print("SELECT Customer.Customer_ID, Customer.Customer_FName, Customer.Customer_MInit, Customer.Customer_LName, Product.Product_ID, Product.Product_Name, Order_Transaction.Order_Quantity, Order_Transaction.Total_Payment, Order_Transaction.Order_Date,(Order_Quantity*Total_Payment) as Bill \
		FROM Customer, Product, Order_Transaction \
		WHERE Product.Product_ID=Order_Transaction.Product_ID and Customer.Customer_ID=Order_Transaction.Customer_ID  AND Customer.Customer_ID=%s AND Product.Product_ID=%s \
		order by Order_Date;")
	mycursor.execute("SELECT Customer.Customer_ID, Customer.Customer_FName, Customer.Customer_MInit, Customer.Customer_LName, Product.Product_ID, Product.Product_Name, Order_Transaction.Order_Quantity, Order_Transaction.Total_Payment, Order_Transaction.Order_Date,(Order_Quantity*Total_Payment) as Bill \
		FROM Customer, Product, Order_Transaction \
		WHERE Product.Product_ID=Order_Transaction.Product_ID and Customer.Customer_ID=Order_Transaction.Customer_ID  AND Customer.Customer_ID=%s AND Product.Product_ID=%s \
		order by Order_Date;")

	mydatabase.commit()
 
	


def add_new_inventory_details():
	print("Enter note for product")
	Note = input()
	print(Note)

	print("UPDATE inventory set Note = 'Needs re-order soon' where instock_quantity <='5';")
	mycursor.execute("UPDATE inventory set Note = 'Needs re-order soon' where instock_quantity <='5';")

	mydatabase.commit()

def add_new_prodcut_details(): 
	print("Enter new prodcut ID")
	Product_ID = input()
	print(Product_ID)
	print("Enter new product name")
	Product_name = input()
	print(Product_name)
	print("Enter new product description")
	Product_description = input()
	print(Product_description)
	print("Enter new prodcut colour")
	Product_colour = input()
	print(Product_colour)
	print("Enter new product type (Guitar,Keyboard,Drums)")
	Product_type = input()
	print(Product_type)
	print("Enter new product purchase price")
	Product_purchase_price = input()
	print(Product_purchase_price)
	print("Enter new product retail price")
	Product_retail_price = input()
	print(Product_retail_price)
	
	print("INSERT INTO Product VALUES (Product_ID, Product_Name, Product_Description,Prodcut_Colour, Product_Type, Product_Price, Retail_Price)")
	mycursor.execute("INSERT INTO Product VALUES (Product_ID, Product_Name, Product_Description, Prodcut_Colour, Product_Type, Product_Price, Retail_Price)")

	mydatabase.commit()

def add_purchase_information(): 
	print("Enter required product ID")
	Product_ID = input()
	print(Product_ID)
	print("Enter specifc supplier ID for required product")
	Supplier_ID = input()
	print(Supplier_ID)
	print("Enter purchase quantity")
	Purchase_Quantity = input()
	print(Purchase_quantity)
	print("Enter Purchase date (YY-MM-DD)")
	Purchase_Date = input()
	print(Purchase_Date)
	
	print("INSERT INTO Purchase_Transaction VALUES (NULL, Product_ID, Supplier_ID, Purchase_Quantity, Purchase_Date)")
	mycursor.executeprint("INSERT INTO Purchase_Transaction VALUES (NULL, Product_ID, Supplier_ID, Purchase_Quantity, Purchase_Date)")
	print("UPDATE Inventory SET InStock_Quantity = InStock_Quantity + (SELECT Purchase_Quantity FROM Purchase_Transaction  WHERE Purchase_Transaction.Product_ID = Inventory.Product_ID)")
	mycursor.execute("UPDATE Inventory SET InStock_Quantity = InStock_Quantity + (SELECT Purchase_Quantity FROM Purchase_transaction  WHERE Purchase_Transaction.Product_ID = Inventory.Product_ID)")
	print("UPDATE Inventory SET Stockup_Date = (SELECT Purchase_Date FROM Purchase_Transaction  WHERE Inventory.Product_ID = Purchase_Transaction.Product_ID)")
	mycursor.execute("UPDATE Inventory SET Stockup_Date = (SELECT Purchase_Date FROM Purchase_Transaction  WHERE Inventory.Product_ID = Purchase_Transaction.Product_ID)")
	print("SELECT Purchase_Transaction.Purchase_ID, Purchase_Transaction.Supplier_ID, Supplier.Supplier_Name, Product.Product_ID,product.Product_Name, Purchase_Transaction.Purchase_Quantity, Product.Purchase_Price, (Purchase_Quantity*Purchase_Price) as Bill, Purchase_Transaction.Purchase_Date \
		from Purchase_Transaction, Supplier, Product \
		where Purchase_Transaction.Product_ID=Product.Product_ID and Purchase_Transaction.Supplier_ID=Supplier.Supplier_ID=%s;")
	mycursor.execute("SELECT Purchase_Transaction.Purchase_ID, Purchase_Transaction.Supplier_ID, Supplier.Supplier_Name, Product.Product_ID,product.Product_Name, Purchase_Transaction.Purchase_Quantity, Product.Purchase_Price, (Purchase_Quantity*Purchase_Price) as Bill, Purchase_Transaction.Purchase_Date \
		from Purchase_Transaction, Supplier, Product \
		where Purchase_Transaction.Product_ID=Product.Product_ID and Purchase_Transaction.Supplier_ID=Supplier.Supplier_ID=%s;")

	mydatabase.commit()

def View_customers():
	print("SELECT * FROM Customer")
	mycursor.execute("SELECT * FROM Customer")

	mydatabase.commit()

def View_suppliers():
	print("SELECT * FROM Supplier")
	mycursor.execute("SELECT * FROM Supplier")

	mydatabase.commit()

def View_inventory():
	print("SELECT * FROM Inventory")
	mycursor.execute("SELECT * FROM Inventory")

	mydatabase.commit()

def View_products():
	print("SELECT * FROM Product")
	mycursor.execute("SELECT * FROM Product")

	mydatabase.commit()

def View_Order_transactions():
	print("SELECT * FROM Order_Transaction")
	mycursor.execute("SELECT * FROM Order_Transaction")

	mydatabase.commit()
	
def Purchase_transaction():
	print("SELECT * FROM Purchase_Transaction")
	mycursor.execute("SELECT * FROM Purchase_Transaction")

	mydatabase.commit()

#mydatabase.commit()

##Creating Queries
def create_customer_invoice():
	print("Enter customer ID you want to generate an invoice for")
	Customer_ID = input("Enter")
	print(Customer_ID)
	print("Enter the assosiated product ID ")
	Product_ID= input("Enter")
	print(Product_ID)
	print("Enter the date of the transaction (YY-MM-DD)")
	Date = input("Enter")
	print(Date)

	print("SELECT Customer.Customer_ID, Customer.Customer_FName, Customer.Customer_MInit, Customer.Customer_LName, Product.Product_ID, Product.Product_Name, Order_Transaction.Order_Quantity, Order_Transaction.Total_Payment, Order_Transaction.Order_Date,(Order_Quantity*Total_Payment) as Bill \
		FROM Customer, Product, Order_Transaction \
		WHERE Product.Product_ID=Order_Transaction.Product_ID and Customer.Customer_ID=Order_Transaction.Customer_ID  AND Customer.Customer_ID=%s AND Product.Product_ID=%s \
		order by Order_Date;" % (Customer_ID, Product_ID))
	mycursor.execute("SELECT Customer.Customer_ID, Customer.Customer_FName, Customer.Customer_MInit, Customer.Customer_LName, Product.Product_ID, Product.Product_Name, Order_Transaction.Order_Quantity, Order_Transaction.Total_Payment, Order_Transaction.Order_Date,(Order_Quantity*Total_Payment) as Bill \
		FROM Customer, Product, Order_Transaction \
		WHERE Product.Product_ID=Order_Transaction.Product_ID and Customer.Customer_ID=Order_Transaction.Customer_ID  AND Customer.Customer_ID=%s AND Product.Product_ID=%s \
		order by Order_Date;" % (Customer_ID, Product_ID))

	for tuple_ in mycursor:
		print(tuple_)

	create_customer_invoice()

	mydatabase.commit()


#search specific supplier invoice
def create_supplier_invoice():
	print("Enter Supplier ID you would like the invoice to be generated for")
	Supplier_ID = input()
	print(Supplier_ID)
	print("Enter the specific Product ID assosiated with the supplier")
	Product_ID = input()
	print(Product_ID)

	print("SELECT Purchase_Transaction.Purchase_ID, Purchase_Transaction.Supplier_ID, Supplier.Supplier_Name, Product.Product_ID,product.Product_Name, Purchase_Transaction.Purchase_Quantity, Product.Purchase_Price, (Purchase_Quantity*Purchase_Price) as Bill, Purchase_Transaction.Purchase_Date \
		from Purchase_Transaction, Supplier, Product \
		where Purchase_Transaction.Product_ID=Product.Product_ID and Purchase_Transaction.Supplier_ID=Supplier.Supplier_ID AND Supplier.Supplier_ID=%s AND Product.Product_ID=%s;" % (Supplier_ID, Product_ID)
	mycursor.execute("SELECT Purchase_Transaction.Purchase_ID, Purchase_Transaction.Supplier_ID, Supplier.Supplier_Name, Product.Product_ID,product.Product_Name, Purchase_Transaction.Purchase_Quantity, Product.Purchase_Price, (Purchase_Quantity*Purchase_Price) as Bill, Purchase_Transaction.Purchase_Date \
		from Purchase_Transaction, Supplier, Product \
		where Purchase_Transaction.Product_ID=Product.Product_ID and Purchase_Transaction.Supplier_ID=Supplier.Supplier_ID AND Supplier.Supplier_ID=%s AND Product.Product_ID=%s;" % (Supplier_ID, Product_ID)

	for tuple_ in mycursor:
		print(tuple_)

	create_supplier_invoice()

	mydatabase.commit()

###########Exclude this part###############
#Dummy (dummy)
def grosss_profittttt_statement():
	print("Select SUM((retail_price*order_quantity)-(purchase_price*order_quantity))\
	From product, order_transaction \
	Where product.product_id=order_transaction.product_ID;")
	


#Dummy
def grosssss1_profittttt_statement():
	print("SELECT SUM((retail_price*Order_Quantity)-(Purchase_Price*Order_Quantity))\
		FROM Product, Order_transaction \
		WHERE Product.Product_ID=Order_Transaction.Product_ID;")
	mycursor.execute("SELECT SUM((retail_price*Order_Quantity)-(Purchase_Price*Order_Quantity))\
		FROM Product, Order_transaction \
		WHERE Product.Product_ID=Order_Transaction.Product_ID;")

	for tuple_ in mycursor:
	 		print(tuple_)

########### Exclude this part###############
	

#Create Gross Profit statement
def gross_profit_statement():
	print("SELECT SUM((retail_price*Order_Quantity)-(Purchase_Price*Order_Quantity))\
		FROM Product, Order_transaction \
		WHERE Product.Product_ID=Order_Transaction.Product_ID;")
	mycursor.execute("SELECT SUM((retail_price*Order_Quantity)-(Purchase_Price*Order_Quantity))\
		FROM Product, Order_transaction \
		WHERE Product.Product_ID=Order_Transaction.Product_ID;")

	for tuple_ in mycursor:
	 		print(tuple_)

	gross_profit_statement()

	mydatabase.commit()

#Create Low end product segment sorted by product type
def low_end_product():
	print("SELECT product_ID, product_name, product_type, retail_price \
		from product \
		where retail_price < '500'  order by product_type;")
	mycursor.execute("SELECT product_ID, product_name, product_type, retail_price \
		from product \
		where retail_price < '500'  order by product_type;")

	for tuple_ in mycursor:
	 		print(tuple_)

	low_end_product()

	mydatabase.commit()

#Create Mid level product segement sorted by prodcut type
def mid_level_product():
	print("SELECT product_ID, product_name, product_type, retail_price \
		from product \
		where retail_price between '500' and '1500'  order by product_type;")
	mycursor.execute("SELECT product_ID, product_name, product_type, retail_price \
		from product \
		where retail_price between '500' and '1500'  order by product_type;")

	for tuple_ in mycursor:
	 		print(tuple_)

	mid_level_product()

	mydatabase.commit()

#Create Mid level product segement sorted by prodcut type
def high_end_product():
	print("SELECT product_ID, product_name, product_type, retail_price \
		from product \
		where retail_price > '1500' order by product_type;")
	mycursor.execute("SELECT product_ID, product_name, product_type, retail_price \
		from product \
		where retail_price > '1500' order by product_type;")

	for tuple_ in mycursor:
	 		print(tuple_)

	high_end_product()

	mydatabase.commit()

# Search to check order history from supplier
def order_history_supplier():
	print("SELECT purchase_transaction.supplier_Id, supplier.supplier_name, purchase_transaction.product_ID, product.product_name, purchase_transaction.Purchase_quantity, SUM(purchase_quantity) as Total_Quantity_Purchase \
	from purchase_transaction, supplier, product \
	where purchase_transaction.supplier_ID=supplier.Supplier_ID and purchase_transaction.product_ID=product.Product_ID \
	group by Supplier_name, Product_ID")
	mycursor.execute("SELECT purchase_transaction.supplier_Id, supplier.supplier_name, purchase_transaction.product_ID, product.product_name, purchase_transaction.Purchase_quantity, SUM(purchase_quantity) as Total_Quantity_Purchase \
	from purchase_transaction, supplier, product \
	where purchase_transaction.supplier_ID=supplier.Supplier_ID and purchase_transaction.product_ID=product.Product_ID \
	group by Supplier_name, Product_ID")

	for tuple_ in mycursor:
	 		print(tuple_)

	order_history_supplier()

	mydatabase.commit()

# Suppliers are contacted when Inventory level goes below 5. So we want an Inventory check of products that have stock level of 5 or below.
def supplier_low_inventory():
	print("SELECT inventory.product_ID, product.product_name, inventory.instock_quantity, purchase_transaction.supplier_ID, supplier.supplier_name, supplier_phone.supplier_phone \
		from inventory, product, purchase_transaction, supplier, supplier_phone \
where inventory.product_ID=product.product_ID and product.product_ID=purchase_transaction.product_id and purchase_transaction.supplier_ID=supplier.supplier_ID and supplier.supplier_ID=supplier_phone.supplier_ID and instock_quantity <='5';")
	mycursor.execute("SELECT inventory.product_ID, product.product_name, inventory.instock_quantity, purchase_transaction.supplier_ID, supplier.supplier_name, supplier_phone.supplier_phone \
		from inventory, product, purchase_transaction, supplier, supplier_phone \
where inventory.product_ID=product.product_ID and product.product_ID=purchase_transaction.product_id and purchase_transaction.supplier_ID=supplier.supplier_ID and supplier.supplier_ID=supplier_phone.supplier_ID and instock_quantity <='5';")

	for tuple_ in mycursor:
	 		print(tuple_)

	supplier_low_inventory()

	mydatabase.commit()

# Customers who purchases over $2000 worth product are given a coupon for $100 discount in their next purchase. Let's create a query to identify these customers 
def customers_discount():
	print("SELECT order_transaction.customer_id, customer.customer_Fname, customer.customer_minit, customer.customer_lname, customer.customer_email \
	from order_transaction, customer \
where order_transaction.customer_ID=customer.customer_ID group by customer_id having sum(total_payment)>'2000';")
	mycursor.execute("SELECT order_transaction.customer_id, customer.customer_Fname, customer.customer_minit, customer.customer_lname, customer.customer_email \
	from order_transaction, customer \
where order_transaction.customer_ID=customer.customer_ID group by customer_id having sum(total_payment)>'2000';")

	for tuple_ in mycursor:
	 		print(tuple_)

	customers_discount()

	mydatabase.commit()

# We can check which product type has the highest quantity sold to decide which product_type requires higher assortment 
def analysis_product_type():
	print("SELECT product.product_type, SUM(order_quantity) as Total_Quantity \
	from product, order_transaction \
	where product.product_ID=order_transaction.product_ID group by product_type;")
	mycursor.execute("SELECT product.product_type, SUM(order_quantity) as Total_Quantity \
	from product, order_transaction \
	where product.product_ID=order_transaction.product_ID group by product_type;")

	for tuple_ in mycursor:
	 		print(tuple_)

	analysis_product_type()

	mydatabase.commit()

# A query to see which customers are actively buying guitars so that we can target these customers when there is an offer on Guitar sections
def highest_customers_for_guitar():
	print("SELECT order_transaction.customer_ID, customer.Customer_fname, customer.customer_minit, customer.customer_lname, customer.customer_email, count(product.product_type) \
from order_transaction, customer, product \
where order_transaction.customer_ID=customer.customer_ID and order_transaction.product_ID=product.product_id and product_type='Guitar' having count(product_type)>1;")
	mycursor.execute("SELECT order_transaction.customer_ID, customer.Customer_fname, customer.customer_minit, customer.customer_lname, customer.customer_email, count(product.product_type) \
from order_transaction, customer, product \
where order_transaction.customer_ID=customer.customer_ID and order_transaction.product_ID=product.product_id and product_type='Guitar' having count(product_type)>1;")

	for tuple_ in mycursor:
			print(tuple_)

	highest_customers_for_guitar()

	mydatabase.commit()

# A query to see which customers are actively buying keyboard so that we can target these customers when there is an offer on Keyboard sections
def highest_customers_for_keyboard():
	print("SELECT order_transaction.customer_ID, customer.Customer_fname, customer.customer_minit, customer.customer_lname, customer.customer_email, count(product.product_type) \
from order_transaction, customer, product \
where order_transaction.customer_ID=customer.customer_ID and order_transaction.product_ID=product.product_id and product_type='keyboard' having count(product_type)>1;")
	mycursor.execute("SELECT order_transaction.customer_ID, customer.Customer_fname, customer.customer_minit, customer.customer_lname, customer.customer_email, count(product.product_type) \
from order_transaction, customer, product \
where order_transaction.customer_ID=customer.customer_ID and order_transaction.product_ID=product.product_id and product_type='keyboard' having count(product_type)>1;")

	for tuple_ in mycursor:
			print(tuple_)

	highest_customers_for_keyboard()

	mydatabase.commit()

# A query to see which customers are actively buying drums so that we can target these customers when there is an offer on Drums sections
def highest_customers_for_drum():
	print("SELECT order_transaction.customer_ID, customer.Customer_fname, customer.customer_minit, customer.customer_lname,  customer.customer_email, count(product.product_type) \
from order_transaction, customer, product \
where order_transaction.customer_ID=customer.customer_ID and order_transaction.product_ID=product.product_id and product_type='drums' having count(product_type)>1;")
	mycursor.execute("SELECT order_transaction.customer_ID, customer.Customer_fname, customer.customer_minit, customer.customer_lname,  customer.customer_email, count(product.product_type) \
from order_transaction, customer, product \
where order_transaction.customer_ID=customer.customer_ID and order_transaction.product_ID=product.product_id and product_type='drums' having count(product_type)>1;")

	for tuple_ in mycursor:
	 		print(tuple_)

	highest_customers_for_drum()

	mydatabase.commit()


#Running code to  ask user what they would like to do
while True:
	print("Please select an option. This will get you access to enter, search and edit data:")
	print("0. Exit - This will take you back to the main menu")
	print("1. Add a new customer and sales details for the purchase")
	print("2. Add purchase information for an existing customer")
	print("3. Add a new supplier and purchase details")
	print("4. Add purchase information for re-ordering products from an existing supplier")
	print("5. Add new products")
	print("6. View if there is a note for low quantity in any of the products")
	print("7. View current products we are selling and information about the same")
	print("8. View current customers")
	print("9. View current suppliers")
	print("10. View Purchase transactions of all customers")
	print("11. View order detail from all suppliers")
	print("12. View customer invoice of a specific customer")
	print("13. View purchase transaction from a specific supplier")
	print("14. Create gross profit statement")
	print("15. Show products in the low-end segement arranged by product type")
	print("16. Show products in the Mid-end segement arranged by product type")
	print("17. Show products in the High-end segement arranged by product type")
	print("18. Show order history from suppliers")
	print("19. Show products that have inventory less than 5. You can then go and add a note to order that product.")
	print("20. Search customers who have purchased more than $2000, to give them a $100 coupon")
	print("21. Which prodcut did we sell the most?")
	print("22. Show customers who purchased the most guitars")
	print("23. Show customers who purchased the most Keyboard")
	print("24. Show customers who purchased the most drums")
	

	choice = input()
	if(choice == '0'):
		mycursor.close()
		mydatabase.close()
		break
	elif(choice == '1'):
		add_new_customer()

	elif(choice == '2'):
		add_new_transaction_details()

	elif(choice == '3'):
		add_new_supplier()

	elif(choice == '4'):
		add_purchase_information()

	elif(choice == '5'):
		add_new_prodcut_details()

	elif(choice == '6'):
		add_new_inventory_details()

	elif(choice == '7'):
		View_products()

	elif(choice == '8'):
		View_customers()

	elif(choice == '9'):
		View_suppliers()

	elif(choice == '10'):
		View_Order_transactions()

	elif(choice == '11'):
		Purchase_transaction()

	elif(choice == '12'):
		create_customer_invoice()

	elif(choice == '13'):
		create_supplier_invoice()

	elif(choice == '14'):
		gross_profit_statement()

	elif(choice == '15'):
		low_end_product()

	elif(choice == '16'):
		mid_level_product()

	elif(choice == '17'):
		high_level_product()

	elif(choice == '18'):
		order_history_supplier()

	elif(choice == '19'):
		supplier_low_inventory()

	elif(choice == '20'):
		customers_discount()

	elif(choice == '21'):
		analysis_product_type()

	elif(choice == '22'):
		highest_customers_for_guitar()

	elif(choice == '23'):
		highest_customers_for_keyboard()

	elif(choice == '24'):
		highest_customers_for_drum()

























