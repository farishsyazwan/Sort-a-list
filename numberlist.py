numberlist=[]
def sort():
    sorting=input("Ascending or Descending or Original?")
    if sorting=="Ascending":
        numberlist.sort()
        print(numberlist)
    elif sorting=="Descending":
        numberlist.sort(reverse=True)
        print(numberlist)
    elif sorting=="Original":
        print(numberlist)
    else:
        sort()
def num():
    x=int(input("Add a number: "))
    numberlist.append(x)
    y=input("Add another number? (Yes or No)")
    if y=="Yes":
        num()
    if y=="No":
        sort()
num()