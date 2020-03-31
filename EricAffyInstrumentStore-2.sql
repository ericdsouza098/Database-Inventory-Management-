-- First we shall create the Database Schema for "Eric & Affy Music Store" Sales and Inventory Management -- 

CREATE database EricAffyInstrumentStore

-- Now we shall create the necessary tables needed. We will insert data as soon as tables are created --

-- Let's create the Product Table -- 
CREATE TABLE Product(
Product_ID INT(4) NOT NULL AUTO_INCREMENT,
Product_Name VARCHAR(20) NOT NULL UNIQUE,
Product_Description VARCHAR(50),
Product_Color VARCHAR(20),
Product_Type VARCHAR(10) NOT NULL CHECK (Product_Type IN ('Guitar','Keyboard','Drums')),
Purchase_Price DECIMAL(10,2) NOT NULL,
Retail_Price DECIMAL(10,2) NOT NULL,
constraint Product_ID_PK primary key (Product_ID)
);

Desc Product
SELECT * FROM Product

-- Let's create Supplier table -- 
CREATE TABLE Supplier(
Supplier_ID INT(6) NOT NULL AUTO_INCREMENT,
Supplier_Name VARCHAR(20) NOT NULL UNIQUE,
Supplier_Street VARCHAR(30),
Supplier_City VARCHAR(20),
Supplier_State VARCHAR(2),
Supplier_Postal VARCHAR(30),
constraint Supplier_PK primary key (Supplier_ID)
);

Desc Supplier
SELECT * FROM Supplier

-- Since Supplier Phone has mutliple values, we will create a separate Supplier's Phone table--
CREATE TABLE Supplier_Phone(
Supplier_ID INT(6) NOT NULL,
Supplier_Phone VARCHAR(20) NOT NULL,
constraint Supplier_Phone_PK primary key (Supplier_Id,Supplier_Phone),
constraint Supplier_Phone_FK foreign key (Supplier_ID) references
Supplier(Supplier_ID)
);

Desc Supplier_Phone
SELECT * FROM Supplier_Phone

-- We will create the Purchase Transaction Table. This table records purchase transactions related to buying the products from Suppliers --
CREATE TABLE Purchase_Transaction(
Purchase_ID INT(5) NOT NULL AUTO_INCREMENT,
Product_ID INT(4) NOT NULL,
Supplier_ID INT(6) NOT NULL,
Purchase_Quantity INT(10) NOT NULL,
Purchase_Date DATE NOT NULL,
constraint Purchase_Transaction_PK primary key (Purchase_ID),
constraint Purchase_Transaction_FK foreign key (Product_ID) references Product(Product_ID),
constraint Purchase_Transaction_FK2 foreign key (Supplier_ID) references Supplier(Supplier_ID)
);

Desc Purchase_Transaction
SELECT*FROM Purchase_Transaction


-- Let's create the Inventory table. This table will provide relevant information regarding the different SKUs available for customers to purchase --
CREATE TABLE Inventory(
Product_ID INT(4) NOT NULL,
Stockup_Date DATE,
InStock_Quantity INT(10),
Note VARCHAR(100),
constraint Inventory_PK primary key (Product_ID), 
constraint Product_ID_FK foreign key (Product_ID) references
Product(Product_ID)
);

Desc Inventory
SELECT* FROM Inventory

-- Now we shall create the Customer table containing relevant information about customers --
CREATE TABLE Customer(
Customer_ID INT(7) NOT NULL AUTO_INCREMENT,
Customer_FName VARCHAR(10) NOT NULL,
Customer_MInit VARCHAR(1),
Customer_LName VARCHAR(10) NOT NULL,
Customer_Street VARCHAR(30),
Customer_City VARCHAR(20),
Customer_State VARCHAR(2),
Customer_Postal VARCHAR(30),
Customer_Email VARCHAR(50) NOT NULL,
constraint CUSTOMER_ID_PK primary key (Customer_ID)
);

Desc Customer
SELECT*FROM Customer


-- Since a customer can have more than one number, we will create a separate table for their phone number --
CREATE TABLE Customer_Phone(
Customer_ID INT(7) NOT NULL,
Customer_Phone VARCHAR(20) NOT NULL,
constraint Customer_Phone_PK primary key (Customer_Id, Customer_Phone),
constraint Customer_Phone_FK foreign key (Customer_ID) references
Customer(Customer_ID)
);

Desc Customer_Phone
SELECT*FROM Customer_Phone


-- Now that we have all the necessary tables to get the complete picture of a sales transaction, we can create the Order Transaction table.
CREATE TABLE Order_Transaction(
Order_ID INT(7) NOT NULL AUTO_INCREMENT,
Order_Date DATE NOT NULL,
Order_Quantity INT(10) NOT NULL,
Product_ID INT(4) NOT NULL,
Customer_ID INT(7) NOT NULL,
Total_Payment Decimal(10,2) NOT NULL,
constraint Order_Transaction_PK primary key (Order_ID),
constraint Order_Transaction_FK1 foreign key (Product_ID) references Product(Product_ID),
constraint Order_Transaction_FK2 foreign key (Customer_ID) references Customer(Customer_ID)
);

Desc Order_Transaction
SELECT*FROM Order_Transaction


-- Now that all the tables are formed, let's insert data --
-- Let's enter data into Product Table --
insert into Product values (NULL,'Fender Squier', 'Tele Special Edition. 6 String Electric Guitar ', 'Butterscotch Blonde',
'Guitar','100.25','299.99');
insert into Product values (NULL,'Gibson Les Paul II', 'Les Paul Standard 60. 6 String Electric Guitar ', 'Sunburst',
'Guitar','300','700');
insert into Product values (NULL,'Korg SV-2', 'Vintage Piano. 73 Key', 'Black',
'Keyboard','1599.99','2999.99');
insert into Product values (NULL,'Roland 100BK', 'Piano Bench', 'Matt Black',
'Keyboard','120.5','150.5');
insert into Product values (NULL,'Yamaha Classic', '4 Piece Set', 'Raven Black',
'Drums','2250','3999.99');
insert into Product values (NULL,'Pearl Standard', '6 Piece Set', 'Brown Wood',
'Drums','3500','6255.5');

-- Let's enter Purchase_Transaction data --
insert into Purchase_Transaction values (NULL,'1', '1', '10',
'2020-02-1');
insert into Purchase_Transaction values (NULL,'2', '2', '8',
'2020-02-1');
insert into Purchase_Transaction values (NULL,'3', '3', '5',
'2020-03-3');
insert into Purchase_Transaction values (NULL,'4', '4', '4',
'2020-03-3');
insert into Purchase_Transaction values (NULL,'5', '5', '3',
'2020-02-1');
insert into Purchase_Transaction values (NULL,'6', '6', '2',
'2020-04-1');

-- Let's enter data for Supplier --
insert into Supplier values (NULL,'Fender', '303 Cook Road', 'North York',
'ON','M3J3T2');
insert into Supplier values (NULL,'Gibson', '100 Hilary Ave', 'Brampton',
'ON','N13KO7');
insert into Supplier values (NULL,'Korg', '10 Kingston Street', 'Kingston',
'NB','B23MY9');
insert into Supplier values (NULL,'Roland', '7 Hillcrest Street', 'Mount Chill',
'BC','V10T9M');
insert into Supplier values (NULL,'Yamaha', '56 Summerhill Rue', 'Montreal',
'QC','X10KP9');
insert into Supplier values (NULL,'Pearl', '45 Don Mount Road', 'Whistler',
'BC','L17KT9');

-- Let's insert data in Supplier_Phone table --
insert into Supplier_Phone values ('1','657-899-2034');
insert into Supplier_Phone values ('2','657-129-2034');
insert into Supplier_Phone values ('3','457-199-4034');
insert into Supplier_Phone values ('4','457-659-7065');
insert into Supplier_Phone values ('5','557-894-8967');
insert into Supplier_Phone values ('5','447-6932-1003');
insert into Supplier_Phone values ('6','547-6932-1004');

-- Let's insert data in Inventory table --
INSERT INTO Inventory VALUES ('1', '2020-02-01', '15','');
INSERT INTO Inventory VALUES ('2', '2020-02-01', '10','');
INSERT INTO Inventory VALUES ( '3','2020-02-03', '5','');
INSERT INTO Inventory VALUES ('4','2020-02-03', '4','');
INSERT INTO Inventory VALUES ('5', '2020-02-01', '3','');
INSERT INTO Inventory VALUES ('6', '2020-02-01', '3','');

-- Let's enter Customer Data --
INSERT INTO Customer VALUES ( Null, 'Satyajit',' ','Ray', '300 Jarvis Junction','Toronto','ON','M23T13','sray@hotmail.com');
INSERT INTO Customer VALUES ( Null, 'Paul','T','Anderson', '23 Night Drive','Toronto','ON','J23U5Z','pta@gmail.com');
INSERT INTO Customer VALUES ( Null, 'Martin','C ','Scorsese', '101 Scorsese Rd','Montreal','QC','N12KL9','scorsese_marty@outlook.com');

-- Let's enter customer phone data --
INSERT INTO Customer_Phone VALUES ( '1', '647-822-8924');
INSERT INTO Customer_Phone VALUES ('2', '417-909-9999');
INSERT INTO Customer_Phone VALUES ( '3', '917-455-8035');

-- Let's enter Order transactions that have occured in the past --
INSERT INTO Order_transaction VALUES ( NULL,'2020-02-20', 2, '1', '1', 299.99);
INSERT INTO Order_transaction VALUES ( NULL,'2020-02-21', 1, '2', '2', 500);
INSERT INTO Order_transaction VALUES ( NULL,'2020-02-21', 1, '3', '3', 2999.99);

-- Now that we have some data and relational tables formed, we can start creating queries --

-- Let's Create Business Case Queries --
-- Let's create Customer Invoices --
create view Customer_Invoice as
Select Customer.Customer_ID, Customer.Customer_FName, Customer.Customer_MInit, Customer.Customer_LName, Product.Product_ID, 
Product.Product_Name, Order_Transaction.Order_Quantity, Order_Transaction.Total_Payment, Order_Transaction.Order_Date,
(Order_Quantity*Total_Payment) as Bill
from Customer, Product, Order_Transaction
where Product.Product_ID=Order_Transaction.Product_ID and Customer.Customer_ID=Order_Transaction.Customer_ID order by Order_Date;

select * from Customer_Invoice

-- Let's Creat Supplier Invoice --
create view Supply_Invoice as
Select Purchase_Transaction.Purchase_ID, Purchase_Transaction.Supplier_ID, Supplier.Supplier_Name, Product.Product_ID,
product.Product_Name, Purchase_Transaction.Purchase_Quantity, Product.Purchase_Price, (Purchase_Quantity*Purchase_Price) as Bill,
Purchase_Transaction.Purchase_Date from Purchase_Transaction, Supplier, Product
where Purchase_Transaction.Product_ID=Product.Product_ID and Purchase_Transaction.Supplier_ID=Supplier.Supplier_ID;

select * from Supply_Invoice

-- Let's create a Gross Profit Statement and Sort it by Product ID -- 
Create view Gross_Profit_Statement_By_Product as
Select Product.Product_ID, Product.Product_Name, Product.Retail_Price, Product.Purchase_Price, 
(Retail_Price - Purchase_Price) as Gross_Margin, Order_Transaction.Order_Quantity,
(Order_Quantity*(Retail_Price - Purchase_Price)) as Total_Gross_Profit
from product, order_transaction
where Product.Product_ID=Order_Transaction.Product_ID;

select * from Gross_Profit_Statement_By_Product

-- Let's create a Gross Profit Statement for the store --
Create view Gross_Profit_Statement_For_Store as
select SUM((retail_price*order_quantity)-(purchase_price*order_quantity)) from product, order_transaction
where product.product_id=order_transaction.product_ID;

select * from Gross_Profit_Statement_For_Store


-- Low end Product Segment sorted by Product Type --
Create view Low_End_Product as
select product_ID, product_name, product_type, retail_price from product
where retail_price < '500'  order by product_type;

-- Mid end Product Segment sorted by Product Type --
Create view Mid_End_Product as
select product_ID, product_name, product_type, retail_price from product
where retail_price between '500' and '1500'  order by product_type;

-- High end Product Segment sorted by Product Type --
Create view High_End_Product as
select product_ID, product_name, product_type, retail_price from product
where retail_price > '1500' order by product_type;

select* from High_End_Product

-- Order History from Supplier --
Create view Order_History_Supplier as
select purchase_transaction.supplier_Id, supplier.supplier_name, purchase_transaction.product_ID,
product.product_name, purchase_transaction.Purchase_quantity, SUM(purchase_quantity) as Total_Quantity_Purchase
from purchase_transaction, supplier, product
where purchase_transaction.supplier_ID=supplier.Supplier_ID and purchase_transaction.product_ID=product.Product_ID 
group by Supplier_name, Product_ID


select*from Order_History_Supplier

-- Suppliers are contacted when Inventory level goes below 5. So we want an Inventory check of products that have stock level of 5 or below --
Create view Stock_To_Be_Ordered_Soon as
select inventory.product_ID, product.product_name, inventory.instock_quantity, purchase_transaction.supplier_ID, 
supplier.supplier_name, supplier_phone.supplier_phone from inventory, product, purchase_transaction, supplier, supplier_phone
where inventory.product_ID=product.product_ID and product.product_ID=purchase_transaction.product_id and
purchase_transaction.supplier_ID=supplier.supplier_ID and supplier.supplier_ID=supplier_phone.supplier_ID
and instock_quantity <='5';

select*from Stock_To_Be_Ordered_Soon

-- Customers who purchases over $2000 worth product are given a coupon for $100 discount in their next purchase. Let's create a query to identify these customers --
create view Customers_Eligible_Coupon as
select order_transaction.customer_id, customer.customer_Fname, customer.customer_minit, customer.customer_lname,
customer.customer_email from order_transaction, customer
where order_transaction.customer_ID=customer.customer_ID
group by customer_id
having sum(total_payment)>'2000';

select*from Customers_Eligible_Coupon

-- We can check which product type has the highest quantity sold to decide which product_type requires higher assortment --
create view Customers_Eligible_Coupon as
select product.product_type, SUM(order_quantity) as Total_Quantity from product, order_transaction
where product.product_ID=order_transaction.product_ID
group by product_type;


-- A query to see which customers actively buying guitars so that we can target these customers when there is an offer on Guitar sections --
Select order_transaction.customer_ID, customer.Customer_fname, customer.customer_minit, customer.customer_lname, customer.customer_email
, count(product.product_type)
from order_transaction, customer, product
where order_transaction.customer_ID=customer.customer_ID and order_transaction.product_ID=product.product_id
and product_type='Guitar'
having count(product_type)>1;

-- A query to see which customers actively buying keyboard so that we can target these customers when there is an offer on Keyboard sections --
Select order_transaction.customer_ID, customer.Customer_fname, customer.customer_minit, customer.customer_lname, customer.customer_email
, count(product.product_type)
from order_transaction, customer, product
where order_transaction.customer_ID=customer.customer_ID and order_transaction.product_ID=product.product_id
and product_type='keyboard'
having count(product_type)>1;

-- A query to see which customers actively buying drums so that we can target these customers when there is an offer on drums sections --
Select order_transaction.customer_ID, customer.Customer_fname, customer.customer_minit, customer.customer_lname,  customer.customer_email
, count(product.product_type)
from order_transaction, customer, product
where order_transaction.customer_ID=customer.customer_ID and order_transaction.product_ID=product.product_id
and product_type='drums'
having count(product_type)>1;









 


