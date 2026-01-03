few_shots = [
  {
    'Question': "How many t-shirts do we have left for Nike in extra small size and white color?",
    'SQLQuery': "SELECT stock_quantity FROM t_shirts WHERE brand = 'Nike' AND size = 'XS' AND color = 'White';",
    'SQLResult': "Result of  the SQL query",
    'Answer': "54"
  },
   {
    'Question': "How much is the price of the inventory for all small size t-shirts?",
    'SQLQuery':"SELECT SUM(price * stock_quantity) AS total_price FROM t_shirts WHERE size = 'S';",
    'SQLResult': "Result of  the SQL query",
    'Answer': "17037"
  },
    {
    'Question': "If we have to sell all the Levi's T-shirts today with discounts applied. How much revenue our store will generate (post discounts)?",
    'SQLQuery':"SELECT SUM((price - (price * pct_discount / 100)) * stock_quantity) AS total_revenue FROM t_shirts JOIN discounts ON t_shirts.t_shirt_id = discounts.t_shirt_id WHERE brand = 'Levi' AND CURDATE() = CURDATE()",
    'SQLResult': "Result of  the SQL query",
    'Answer': "24"
  },
    {
    'Question': "How many white color Levi's t-shirts we have available?",
    'SQLQuery':"SELECT COUNT(*) AS total_available FROM t_shirts WHERE brand = 'Levi' AND color = 'White';",
    'SQLResult': "SELECT SUM(stock_quantity)FROM t_shirts WHERE brand = 'Levi' AND color = 'White';",
    'Answer': "220"
  },
]