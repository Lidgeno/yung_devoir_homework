import mysql.connector
<<<<<<< Updated upstream
mysql=mysql.connector.connect(host="localhost", user="root", passwd="", database="essai")


#toute la table
# Create Table
mycursor.execute('''CREATE TABLE creation(id int, figure_1 VARCHAR(20), figure_2 VARCHAR(20), figure_3 VARCHAR(20), figure_4 VARCHAR(20), figure_5 VARCHAR(20))''')

sql="insert into creation(id, figure_1, figure_2, figure_3, figure_4, figure_5) VALUES (%s,%s,%s,%s,%s,%s)"
for i in range (1,nbfigures):
    val=[
        (liste_figures[i])
        ]
    mycursor.executemany(sql,val)


mysql.commit();

print("la table creation a ete completee");
=======

nbmaxfigures=5
mysql=mysql.connector.connect(host="localhost", user="root", passwd="", database="genese")
mycursor=mysql.cursor()

def enregistrement(liste_figures):
    sql="insert into creation(figure_1, figure_2, figure_3, figure_4, figure_5) VALUES (%s,%s,%s,%s,%s)"
    
    val=[(liste_figures)]
    print(val)
    mycursor.executemany(sql,val)

    mysql.commit();

    print("la table creation a ete completee");
>>>>>>> Stashed changes