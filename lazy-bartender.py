#lazy bartender

from collections import Counter 
drinks = []

no = int(input("Enter No Of Possible Drinks: "))
l = [(i) for i in range(1,no+1)]

c = int(input("No Of Fixed Customers: "))
i=1

count = []

while i < c+1 :
    
    print("Customer {} Drinks :".format(i))
    n = int(input("How Much Drink: "))
    
    for j in range(n):
        
        temp = int(input("ENTER DRINK {}:".format(j)))
        
        if temp <= no:
            count.append(temp)
        elif temp >= no:
            temp = int(input("ENTER DRINK {} AGAIN:".format(j)))
            if temp <= no:
                count.append(temp)
            else:
                print("You're Entering wrong drink")
                break
        
    i+=1    
    

word_counter = Counter(count)
top = word_counter.most_common(3) 
print(top)


for i in top:
    print(i[0])
