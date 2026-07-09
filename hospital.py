import sqlite3

con = sqlite3.connect("hospital.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS patient(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    disease TEXT,
    phone TEXT
)
""")

con.commit()

while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Disease")
    print("5. Delete Patient")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        pid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        disease = input("Enter Disease: ")
        phone = input("Enter Phone: ")

        cur.execute(
            "INSERT INTO patient VALUES(?,?,?,?,?,?)",
            (pid, name, age, gender, disease, phone)
        )

        con.commit()

        print("Patient Added Successfully")

    elif choice == "2":

        cur.execute("SELECT * FROM patient")

        data = cur.fetchall()

        print("\n------ Patient List ------")

        for i in data:
            print(i)

    elif choice == "3":

        pid = int(input("Enter Patient ID: "))

        cur.execute(
            "SELECT * FROM patient WHERE id=?",
            (pid,)
        )

        data = cur.fetchone()

        if data:
            print(data)
        else:
            print("Patient Not Found")

    elif choice == "4":

        pid = int(input("Enter Patient ID: "))
        disease = input("Enter New Disease: ")

        cur.execute(
            "UPDATE patient SET disease=? WHERE id=?",
            (disease, pid)
        )

        con.commit()

        print("Patient Updated Successfully")

    elif choice == "5":

        pid = int(input("Enter Patient ID: "))


        cur.execute(
            "DELETE FROM patient WHERE id=?",
            (pid,)
        )

        con.commit()

        print("Patient Deleted Successfully")

    elif choice == "6":

        print("Thank You")
        break

    else:

        print("Invalid Choice")

con.close()
