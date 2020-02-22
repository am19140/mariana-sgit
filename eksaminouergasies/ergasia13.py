num = list(input("Please enter a credit card number without spaces: "))

num = list(map(int, num))[::-1] 

for index in range(1,len(num),2): #κάθε 2 ψηφία κάνω έλεγχο
    if num[index]<5:
        num[index] = num[index] *2 #αν είναι μεγαλύτερο του 5 πολλαπλασιάζω με 2
    else:
        num[index] = ((num[index]*2)//10) + ((num[index]*2)%10) #αλλιώς πολλαπλασιάζω με το 2: 2 φορές, την πρώτη φορά βρίσκω ακέραιο αποτέλεσμα διαίρεσης με 10 και την δεύτερη το υπολοιπο της.τέλος προσθέτω τους 2 αριθμους
        

checksum=sum(num) # συναρτηση sum για προσθεση ψηφιων του αριθμου που περιεχεται στην μεταβλητη num

print("checksum= {}".format(checksum))

if checksum%10 !=0: #αν το υπολοιπο της διαιρεσης δεν ειναι 0
    print('the number is not valid! Try a different numbber')
else:
    print('the number is valid!')
