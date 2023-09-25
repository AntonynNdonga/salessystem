import psycopg2

try:
    conn = psycopg2.connect("dbname=kassmat  user=postgres  password=123Sugarcane")
    cur = conn.cursor()
except Exception as e:
    print(e)


def fetch_data(tbname):
    try:
        q = "SELECT * FROM " + tbname + ";"
        cur.execute(q)
        records = cur.fetchall()
        return records
    except Exception as e:
        return e


def insert_products(v):
    vs = str(v)
    q = (
        "insert into products(name, buying_price, selling_price, quantity) "
        "values" + vs
    )
    cur.execute(q)
    conn.commit()
    return q


def update_products(vs):
    id = vs[0]
    name = vs[1]
    buying_price = vs[2]
    selling_price = vs[3]
    q = "UPDATE products SET name = %s, buying_price = %s, selling_price = %s WHERE id = %s"
    cur.execute(q, (name, buying_price, selling_price, id))
    conn.commit()
    return q


def delete_products(vs):
    id = vs[0]
    name = vs[1]
    buying_price = vs[2]
    selling_price = vs[3]
    q = "DELETE products SET name = %s, buying_price = %s, selling_price = %s WHERE id = %s"
    cur.execute(q, (name, buying_price, selling_price, id))
    conn.commit()
    return q


def insert_products(v):
    vs = str(v)
    q = "insert into products(name,buying_price,selling_price) " "values" + vs
    cur.execute(q)
    conn.commit()
    return q


def insert_sales(v):
    vs = str(v)
    q = "insert into sales(pid,quantity,created_at) " "values" + vs
    cur.execute(q)
    conn.commit()
    return q


# STORE ALL PRODUCT NAMES IN A LIST AND ONLY PRINT THAT LIST, DO NOT FILTER IN THE QUERRY.
def remaining_stock():
    q = " SELECT * FROM remaining_stock;"
    cur.execute(q)
    results = cur.fetchall()
    return results


def insert_stock(v):
    vs = str(v)
    q = "insert into stock(pid,quantity, created_at) " "values" + vs
    cur.execute(q)
    conn.commit()
    return q


def sales_per_products():
    spquery = "SELECT * FROM sales_per_product"
    cur.execute(spquery)
    qu = cur.fetchall()
    return qu


def sales_per_day():
    q = "SELECT created_at, SUM(quantity) as total_sales FROM sales GROUP BY created_at ORDER BY created_at"
    cur.execute(q)
    results = cur.fetchall()
    return results

# def add_users(full_name, email, password, confirm_password,created_at):
#     if not all([full_name, email, password, confirm_password]):
#         return "Error: Please provide all required information."

#     if password != confirm_password:
#         return "Error: Passwords do not match."

#     q = "INSERT INTO users  (full_name, email, password, confirm_password,created_at) " \
#         "VALUES (%s, %s, %s, %s,%s);"
#     cur.execute(q, (full_name, email, password, confirm_password,created_at))
#     conn.commit()
#     return "User added successfully."



def login():
    q = "SELECT email, password FROM users;"
    cur.execute(q)
    results = cur.fetchall()
    return results


def remainin_stock(product_id=None):
    q = """ SELECT st.quantity - COALESCE(sum(sa.quantity), 0::bigint) AS remaining_stock
     FROM products p
     JOIN stock st ON p.id = st.pid
     LEFT JOIN sales sa ON p.id = sa.pid
     WHERE p.id = %s
    GROUP BY st.quantity;"""
    cur.execute(q, (product_id,))
    results = cur.fetchall()
    if results:
        return results[0]
    else:
        return None


def get_pid():
    q = "SELECT id from products"
    cur.execute(q)
    qu = cur.fetchall()
    return qu


# STORE ALL PRODUCT NAMES IN A LIST AND ONLY PRINT THAT LIST, DO NOT FILTER IN THE QUERRY.
