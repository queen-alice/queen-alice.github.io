SELECT prod_id, vend_id FROM products
SELECT * FROM products
SELECT vend_id FROM product
SELECT DISTINCT vend_id FROM products /*returns the distinct word*/
SELECT TOP(3) prod_name FROM products /*returns the top rows*/
SELECT TOP(25) PERCENT prod_name FROM products /*returns the top percentage rows*/
SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price, prod_name;
SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price DESC;
SELECT TOP(3) prod_id, prod_price, prod_name FROM products ORDER BY prod_price DESC;
SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price DESC, prod_name;
/*Lesson 6 filtering data*/
SELECT prod_name, prod_price FROM products WHERE prod_price = 2.50;
SELECT prod_name, prod_price FROM products WHERE prod_name = 'fuses';
SELECT vend_id, prod_name FROM products WHERE vend_id <> 1003; /*vend_id is not 1003*/
SELECT prod_name FROM products WHERE prod_price IS NULL;
SELECT cust_id FROM customers WHERE cust_email IS NULL;
SELECT prod_id, prod_price, prod_name FROM products WHERE vend_id = 1003 AND prod_price <= 10;
SELECT prod_name, prod_price FROM products WHERE vend_id IN (1002,1003) ORDER BY prod_name;
/*Lesson 8 wildcard filtering data; search against unknown values*/
SELECT prod_id, prod_name FROM products WHERE prod_name LIKE 'jet%';
SELECT prod_id, prod_name FROM products WHERE prod_name LIKE '%anvil%';
SELECT prod_name FROM products WHERE prod_name LIKE 's%e';
SELECT prod_id, prod_name FROM products WHERE prod_name LIKE '_ ton anvil%';
SELECT cust_contact FROM customers WHERE cust_contact LIKE '[EJ]%' ORDER BY cust_contact;
SELECT cust_contact FROM customers WHERE cust_contact LIKE '[^EJ]%' ORDER BY cust_contact;
/*Lesson 9 Calculated Fields */
/* concatnate two columns together; using parenthesis*/
SELECT vend_name + '(' + vend_country + ')' FROM vendors ORDER BY vend_name;
/*The RTrim() function trims all spaces from the right of a value. By using RTrim(), you can trim the individual columns properly*/
SELECT RTrim(vend_name) + '(' + RTrim(vend_country) + ')' FROM vendors ORDER BY vend_name;
/*Concatnate two columns and making a new column called vend_title */
SELECT RTrim(vend_name) + ' (' + RTrim(vend_country) + ')' AS vend_title FROM vendors ORDER BY vend_name;

SELECT prod_id, quantity, item_price 
FROM orderitems 
WHERE order_num = 20005;

SELECT prod_id, quantity, item_price, quantity*item_price AS expanded_price 
FROM orderitems
WHERE order_num = 20005;

/*Lesson 10 Using data manipulation functions*/
/*using the function Upper to make an uppercase column*/
SELECT vend_name, UPPER(vend_name) AS vend_name_upcase FROM vendors ORDER BY vend_name;
SELECT cust_name, cust_contact FROM customers WHERE Soundex(cust_contact) = Soundex('Y Ling');

/*Lesson 12 Group*/
SELECT * FROM orders
SELECT Count(*) FROM products 
SELECT vend_id, Count(*) AS num_prods FROM products GROUP BY vend_id;
SELECT cust_id, Count(*) AS orders FROM orders GROUP BY cust_id;
SELECT cust_id, Count(*) AS orders FROM orders GROUP BY cust_id HAVING Count(*) >= 2
SELECT vend_id, Count(*) AS num_prods FROM products WHERE prod_price >= 10 GROUP BY vend_id
/*group by vs order by*/
/*Having is like WHERE but used after GROUP BY; WHERE filters before data is grouped
HAVING filters data after grouped*/
SELECT order_num, Sum(quantity*item_price) AS ordertotal 
FROM orderitems 
GROUP BY order_num 
HAVING Sum(quantity*item_price) >= 50 ORDER BY ordertotal

/*Lesson 13 Working with Subqueries*/
