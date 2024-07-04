name=input("enter string:")
print("Original string is:",name)
r_name=" "
count=len(name)
while count>0:
    r_name=r_name+name[count-1]
    count=count-1
    print('reversed string is',r_name)