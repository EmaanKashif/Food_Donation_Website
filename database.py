import sqlite3

def connection():
    return sqlite3.connect('food_database.db')

def get_restaurants():
    file = connection()
    create_obj= file.cursor()
    create_obj.execute("DROP TABLE IF EXISTS Restaurant")
    create_obj.execute("""
        CREATE TABLE IF NOT EXISTS Restaurant(
        id INT PRIMARY KEY, 
        name TEXT,
        location TEXT, 
        food_available TEXT,
        pickup_time TEXT)
    """)
    restaurants = [
        (100,"Restaurant 1","MM Alam road, Lhr","Biryani","5pm"),
        (101,"Restaurant 2","Jhang road, Lhr","Hareesa","8pm"),
        (102,"Restaurant 3","Canal road,Fsd","Pizza","10pm"),
        (103,"Restaurant 4","Satiyana road, Fsd","Daal Chawal","2pm"),
        (104,"Restaurant 5","Motorway road,Rwp","Chicken Qorma","6pm"),
        (105,"Restaurant 6","Murre road,Rwp","Pasta","9pm"),
        (106,"Restaurant 7","Korangi road,Karachi","Aloo Qeema","7pm")
    ]
    create_obj.executemany("INSERT INTO Restaurant VALUES(?,?,?,?,?)",restaurants)
    file.commit()
    create_obj.execute("SELECT * FROM Restaurant ")
    data = create_obj.fetchall()
    file.close()
    return data

def get_charities():
    file = connection()
    create_obj = file.cursor()
    create_obj.execute('DROP TABLE IF EXISTS Charity')

    create_obj.execute("""
        CREATE TABLE Charity(
        id INT PRIMARY KEY,
        name TEXT,
        food_requirement TEXT,
        location TEXT)
    """)

    charity_centres = [
        (200,"Charity 1","Daal Chawal","Satiyana road, Fsd"),
        (201,"Charity 2","Pizza","Canal road,Fsd"),
        (202,"Charity 3","Sandwich","Jaranwala road, Fsd"),
        (203,"Charity 4","Hareesa","Jhang road, Lhr"),
        (204,"Charity 5","Biryani","MM Alam road, Lhr"),
        (205,"Charity 6","Aloo Qeema","Korangi road,Karachi"),
        (206,"Charity 7","Fruit Salad","Jinnah Avenue, Isbd")
    ]

    create_obj.executemany("INSERT INTO Charity VALUES(?,?,?,?)",charity_centres)
    file.commit()
    create_obj.execute("SELECT * FROM Charity")
    data = create_obj.fetchall()
    file.close()
    return data
# rows = create_obj.execute("SELECT * FROM Restaurant").fetchall()
# for row in rows:
#     print("Restaurants: ",row)
# for col in columns:
#     print("Charity_centres: ",col)

def get_matches():
    file = connection()
    create_obj = file.cursor()
    create_obj.execute("""
        SELECT 
            r.name AS restaurant_name,
            r.food_available,
            r.pickup_time,
            c.name AS charity_name,
            c.food_requirement,
            c.location
        FROM Restaurant r
        JOIN Charity c
            ON r.food_available = c.food_requirement
            AND r.location = c.location
    """)
    data = create_obj.fetchall()
    file.close()
    return data


# for match in matches:
#     print(f"{match[3]} should pick {match[1]} from {match[0]}  at {match[2]} (Location: {match[4]})")
