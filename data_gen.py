import random

'''
    This is a Python script used to generte fake data for Account,
    Transactions, and Statement
    Author: nlq506
'''
    
# Generate random account number    
def random_account_number():
     acct_num = random.randint(10**10, 10**11)
     return acct_num

# Generate random Dates
def random_date (start_year, end_year, start_month, end_month, start_day, end_day):
    random_year = str(random.randint(start_year, end_year))
    random_month = str(random.randint(start_month, end_month)).rjust(2, '0')
    random_day = str(random.randint(start_day, end_day)).rjust(2, '0')
    if random_day == 30 and random_month == 02:
        random_day = str(random.randint(01, 28)).rjust(2, '0')
    rand_date = random_year + random_month + random_day
    return rand_date

# Generate random transactions ammount
def random_ammount (min_amnt, max_amnt):
    random_ammt = round(random.uniform(min_amnt, max_amnt), 2)
    return random_ammt
 
# Generate a random credit or debit indicator
def random_debit_credit_indicator():
    debit_credit_ind = random.choice("CD")
    return debit_credit_ind

# Generate random merchante category
def random_merchant_category():
     array_merch_catg = [5732, 5944, 4829, 5678, 2314, 9487]
     merch_catg = random.choice(array_merch_catg)
     return merch_catg

# Generate purchase code
def random_purchase_code():
     prch_code = random.randint(1000, 2000)
     return prch_code
 

# Popullate the array with random Account Numbers
def popullate_array(acct_numbers_array, number_acct_fields):
    for i in range(1, number_acct_fields):
        acct_num = random_account_number()
        acct_numbers_array.append(acct_num)
        
    return acct_numbers_array 
 
# Write to a Transactions file
def write_trxn_file(acct_numbers_array, number_trxn_fields, trxn_file_name):
    output_file = open(trxn_file_name,"w")
    
    trxn_start_year = 2015
    trxn_end_year= 2015
    trxn_start_month = 4
    trxn_end_month = 8
    trxn_start_day = 01
    trxn_end_day = 30
    
    min_ammt = 0.01
    max_ammt = 10000.00
    
    for i in range(0,number_trxn_fields):
        acct_num = random.choice(acct_numbers_array)
        trxn_date = random_date(trxn_start_year,trxn_end_year, trxn_start_month, trxn_end_month, trxn_start_day, trxn_end_day)
        deb_cred_indicator = random_debit_credit_indicator()
        merch_catg = random_merchant_category()
        trxn_amnt = random_ammount(min_ammt,max_ammt)
        prch_code = random_purchase_code()
        output_file.write("%s" %acct_num + "\001" + "%s" %trxn_date + "\001" + "%s" %deb_cred_indicator + "\001" + "%s" %merch_catg + "\001"  + "%s" %trxn_amnt +  "\001" + "%s\n" %prch_code)
     
    output_file.close()

# Write to a Statement file
def write_stmt_file(acct_numbers_array, number_stmt_fields, stmt_file_name):
    output_file = open(stmt_file_name,"w")
    
    stmt_start_year = 2015
    stmt_end_year= 2015
    stmt_start_month = 5
    stmt_end_month = 7
    stmt_start_day = 02
    stmt_end_day = 28
   
    for i in range(0,number_stmt_fields):
        acct_num = random.choice(acct_numbers_array)
        stmt_date = random_date(stmt_start_year,stmt_end_year, stmt_start_month, stmt_end_month, stmt_start_day,stmt_end_day)
        output_file.write("%s" %acct_num + "\001" + "%s\n" %stmt_date) 
        
    output_file.close

# Write to a Account file
def write_acct_file (acct_numbers_array, number_acct_fields, acct_file_name):
    output_file = open(acct_file_name, 'w')
    for acct_num in acct_numbers_array:
        output_file.write("%s\n" %acct_num)
    
    output_file.close ()

# Main method
def main ():
    acct_numbers_array = []
    
    trxn_file_name = "data/transactions"
    stmt_file_name = "data/statements"
    acct_file_name = "data/accounts"

    number_acct_fields = 20
    number_stmt_fields = 60
    number_trxn_fields = 80
    
    # Fill the array with random account IDs.
    acct_numbers_array = popullate_array(acct_numbers_array, number_acct_fields)
        
    # Write all the account number to a Account file.
    write_acct_file(acct_numbers_array, number_acct_fields, acct_file_name)
    
    # Write random account numbers choosen from the Array
    # togetehr with statement date to a Statement file.
    write_stmt_file(acct_numbers_array, number_stmt_fields, stmt_file_name)
    
    # Write all the data fields to a Transaction file.
    write_trxn_file(acct_numbers_array, number_trxn_fields, trxn_file_name)
    
main()