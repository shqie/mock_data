import random

    
# Generate random account number    
def random_account_number():
     acct_num = random.randint(10**10, 10**11)
     return acct_num

 
 

for i in range (0, 10):
    acct_num = random_account_number()   
    print (acct_num)
    
    
