import cx_Oracle 
import re
g=input("enter file name")
r=open(g,encoding='utf-8')
ree=r.read()
ch=ree.split()
y=[]
z=[]
for xx1 in ch:
 y.append(xx1)
print("--------TOKENIZED--------")
print(y)
with open('stopwords.txt') as f:
 x=f.read()
 x=x.split()
 for xx in ch:
  if xx not in x:
   z.append(xx)
print("--------STOP WORDS REMOVAL--------")
print(z)
name=[]
with open('name.txt') as f:
 x2=f.read()
 x2=x2.split()
 for xx2 in ch:
  if xx2 in x2:
   name.append(xx2)
print("--------NAME--------")
print(name)
place=[]
with open('state.txt') as f:
 x4=f.read()
 x4=x4.split()
 for xx4 in ch:
  if xx4 in x4:
   place.append(xx4)
print("--------PLACE--------")
print(place)
age=[]
with open('age.txt') as f:
 x3=f.read()
 x3=x3.split()
 for xx3 in ch:
  if xx3 in x3:
   age.append(xx3)
print("--------AGE--------")
print(age)



import cx_Oracle 
  
try: 
  
    con = cx_Oracle.connect('system/sowmya@localhost') 
      
    # Now execute the sqlquery 

    cursor = con.cursor() 
 
       
    stmt="insert into farmer1 values(:nn,:ns,:na)"
    cursor.execute(stmt,nn=name[0],ns=place[0],na=age[0]) 
      
    # commit that insert the provided data 
    con.commit() 
      
    print("value inserted successful") 
  
except cx_Oracle.DatabaseError as e: 
    print("There is a problem with Oracle", e) 
  
# by writing finally if any error occurs 
# then also we can close the all database operation 
finally: 
    if cursor: 
        cursor.close() 
    if con: 
        con.close()  