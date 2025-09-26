#computer project bank management system 
import csv
import tabulate
from tkinter import *
import os


import csv

def create_acc():
    print('*'*30)
    file = open('acount_list.csv', 'a+', newline='')  # Add 'newline=' parameter to avoid blank lines in CSV.
    fw = csv.writer(file)
    fr = csv.reader(file)
    c = 0
    for k in fr:
        c += 1
    acc_no = c + 1
    #fisrt name
    name_first = str.upper(input('enter first name: '))
    while not name_first.isalpha():
        print('wrong name entered, please try again')
        name_first = str.upper(input('enter first name: '))

    #last name
    name_last = str.upper(input('enter last name: '))
    while not name_last.isalpha():
        print('wrong name entered, please try again')
        name_last = str.upper(input('enter last name: '))
    acc_name = [name_first, name_last]

    print('ADDRESS:-')
    #city
    adress_city = str.upper(input('enter city: '))
    while not adress_city.isalpha():
        print('wrong name entered, please try again')
        adress_city = str.upper(input('enter city: '))

    #area
    adress_area = str.upper(input('enter area: '))
    while not adress_area.isalpha():
        print('wrong name entered, please try again')
        adress_area = str.upper(input('enter area: '))

    #block no.
    adress_block = str.upper(input('enter block no.: '))
    while not adress_block.isdigit():
        print('wrong number entered, please try again')
        adress_block = str.upper(input('enter block no.: '))

    #building no.
    adress_bldg = str.upper(input('enter building no.: '))
    while not adress_bldg.isdigit():
        print('wrong number entered, please try again')
        adress_bldg = str.upper(input('enter building no.: '))

    #house no.
    adress_hs = str.upper(input('enter house no.: '))
    while not adress_hs.isdigit():
        print('wrong number entered, please try again')
        adress_hs = str.upper(input('enter house no.: '))
    acc_adress = [adress_city, adress_area, adress_block, adress_bldg, adress_hs]

    print('NUMBERS:-')
    #primary no.
    acc_pr_no = int(input('enter primary mobile no.: '))
    while not str(acc_pr_no).isdigit() or not (8 <= len(str(acc_pr_no)) <= 10):
        print('wrong number entered, please try again')
        acc_pr_no = int(input('enter primary mobile no.: '))

    #secondary no.
    acc_sd_no = int(input('enter secondary mobile no.: '))
    while not str(acc_sd_no).isdigit() or not (8 <= len(str(acc_sd_no)) <= 10):
        print('wrong number entered, please try again')
        acc_sd_no = int(input('enter secondary mobile no.: '))

    #fax no.
    acc_fx_no = int(input('enter fax no.: '))
    while not str(acc_fx_no).isdigit() or not (5 <= len(str(acc_fx_no)) <= 10):
        print('wrong number entered, please try again')
        acc_fx_no = int(input('enter fax no.: '))

    #birthdate of account holder:
    while True:
        acc_bd = str(input('enter birth date [dd/mm/yyyy]: '))
        try:
            day, month, year = map(int, acc_bd.split('/'))
            valid_date = True

            if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
                valid_date = False

            if month in [4, 6, 9, 11] and day > 30:
                valid_date = False

            if month == 2:
                if day > 29:
                    valid_date = False
                if day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                    valid_date = False

            if valid_date and (2023 - year) < 19:
                valid_date = False

            if valid_date:
                break
            else:
                print('wrong date entered, please try again')
        except ValueError:
            print('wrong date format, please try again')

    #account password
    acc_pass = int(input('enter account password: '))
    while not str(acc_pass).isdigit() or not (5 <= len(str(acc_pass)) <= 10):
        print('wrong number entered, please try again')
        acc_pass = int(input('enter account password: '))

    print('*'*30)
    print('account has been created, please deposit some balance to activate...')
    print('*'*30)

    #deposit some money to your account
    while True:
        acc_bal = float(input('enter amount to be deposited: '))
        if acc_bal > 0:
            break
        else:
            print('Please enter a valid amount.')

    acc = [acc_no, acc_name, acc_adress, acc_pr_no, acc_sd_no, acc_fx_no, acc_bd, acc_bal, acc_pass]
    fw.writerow(acc)
    file.close()
    print('*'*30)

def close_acc():
    print('*'*30)
    acc_no = int(input('enter account no. to be closed: '))
    rec = []
    with open('acount_list.csv', 'r') as file:
        fr = csv.reader(file)
        for k in fr:
            if k[0] == str(acc_no):
                c = 0
                for i in range(5):
                    acc_pass = int(input('enter account password: '))
                    if int(k[-1]) == acc_pass:
                        break
                    else:
                        print('wrong password entered.')
                        c += 1
                if c == 5:
                    print('account has been blocked')
                    rec.append(k)
                else:
                    print('account has been successfully closed')
            else:
                rec.append(k)

    with open('acount_list.csv', 'w', newline='') as file:
        fw = csv.writer(file)
        fw.writerows(rec)

    print('*'*30)

def money_withdraw():
    print('*'*30)
    acc_no = input('enter account no. :')
    rec = []
    with open('acount_list.csv', 'r') as file:
        fr = csv.reader(file)
        for k in fr:
            if k[0] == acc_no:
                c = 0
                for i in range(5):
                    acc_pass = int(input('enter account password: '))
                    if int(k[-1]) == acc_pass:
                        amount = float(input('enter withdrawal amount: '))
                        if amount > float(k[-2]):
                            print('insufficient balance, transaction not possible...')
                            break
                        else:
                            k[-2] = float(k[-2]) - amount
                            rec.append(k)
                            break
                    else:
                        print('wrong password entered, try again')
                        c += 1
                if c == 5:
                    print('account has been blocked')
                    rec.append(k)
                else:
                    print('amount has successfully been withdrawn...')
                    print('account balance left:', k[-2])
            else:
                rec.append(k)

    with open('acount_list.csv', 'w', newline='') as file:
        fw = csv.writer(file)
        fw.writerows(rec)

    print('*'*30)

def money_deposit():
    print('*'*30)
    acc_no = input('enter account no. :')
    rec = []
    with open('acount_list.csv', 'r') as file:
        fr = csv.reader(file)
        for k in fr:
            if k[0] == acc_no:
                c = 0
                for i in range(5):
                    acc_pass = input('enter account password: ')
                    if k[-1] == acc_pass:
                        amount = float(input('enter deposit amount: '))
                        k[-2] = float(k[-2]) + amount
                        rec.append(k)
                        break
                    else:
                        print('wrong password entered, try again')
                        c += 1
                if c == 5:
                    print('account has been blocked')
                    rec.append(k)
                else:
                    print('amount has successfully been deposited...')
                    print('updated account balance:', k[-2])
            else:
                rec.append(k)

    with open('acount_list.csv', 'w', newline='') as file:
        fw = csv.writer(file)
        fw.writerows(rec)

    print('*'*30)

def update_acc():
    
    while True:
        print('*'*30)
        print('       UPDATING MENU      ')
        print('*'*30)
        print('1. Name ')
        print('2. Adress ')
        print('3. Phone Number ')
        print('4. Account Password')
        print('0. back...')
        print('*'*30)
        ch=int(input('enter your selection :'))
        print('*'*30)
        if ch==1:
            file = open('acount_list.csv','r')
            fr=csv.reader(file)
            acc_no=int(input('enter account no. :'))
            rec=[]
            for k in fr:
                if k[0]==acc_no:
                    name_first=str.upper(input('enter new first name :'))
                    while True:                        
                        if name_first.isalpha() != True:
                            print('wrong name entered , please try again')
                            print()
                            name_first=str.upper(input('enter new first name :'))
                            if name_first.isalpha() == True: 
                                k[1][0]=name_first                                
                                break
                        else: 
                            k[1][0]=name_first
                            break 

                    name_first=str.upper(input('enter new last name :'))
                    while True:                        
                        if name_first.isalpha() != True:
                            print('wrong name entered , please try again')
                            print()
                            name_first=str.upper(input('enter new last name :'))
                            if name_first.isalpha() == True: 
                                k[1][1]=name_first                                
                                break
                        else: 
                            k[1][1]=name_first 
                            break
                    rec.append(k)
                else: rec.append(k)
            file.close()
            file = open('acount_list.csv','w')
            fw=csv.writer(file)
            fw.writerows(rec)
            file.close()
            print('*'*30)

        if ch==2:
            file = open('acount_list.csv','r')
            fr=csv.reader(file)
            acc_no=int(input('enter account no. :'))
            rec=[]
            #acc_adress=[adress_city,adress_area,adress_block,adress_bldg,adress_hs]
            for k in fr:
                if k[0]==acc_no:
                    name_first=str.upper(input('enter new city name :'))
                    while True:                        
                        if name_first.isalpha() != True:
                            print('wrong name entered , please try again')
                            print()
                            name_first=str.upper(input('enter new city name :'))
                            if name_first.isalpha() == True: 
                                k[2][0]=name_first                                
                                break
                        else: 
                            k[2][0]=name_first
                            break
                    
                    name_first=str.upper(input('enter new area name :'))
                    while True:
                        
                        if name_first.isalpha() != True:
                            print('wrong name entered , please try again')
                            print()
                            name_first=str.upper(input('enter new area name :'))
                            if name_first.isalpha() == True: 
                                k[2][1]=name_first                                
                                break
                        else: 
                            k[2][1]=name_first
                            break
                    
                    name_first=str.upper(input('enter new block no. :'))
                    while True:                        
                        if name_first.isdigit() != True:
                            print('wrong number entered , please try again')
                            print()
                            name_first=str.upper(input('enter new block no. :'))
                            if name_first.isdigit() == True: 
                                k[2][2]=name_first                                
                                break
                        else: 
                            k[2][2]=name_first
                            break

                    name_first=str.upper(input('enter new building no. :'))
                    while True:                        
                        if name_first.isdigit() != True:
                            print('wrong number entered , please try again')
                            print()
                            name_first=str.upper(input('enter new building no. :'))
                            if name_first.isdigit() == True: 
                                k[2][3]=name_first                                
                                break
                        else: 
                            k[2][3]=name_first
                            break

                    name_first=str.upper(input('enter new house no. :'))
                    while True:                        
                        if name_first.isdigit() != True:
                            print('wrong number entered , please try again')
                            print()
                            name_first=str.upper(input('enter new house no. :'))
                            if name_first.isdigit() == True: 
                                k[2][4]=name_first                                
                                break
                        else: 
                            k[2][4]=name_first
                            break
                    rec.append(k)
                else: rec.append(k)    



            file.close()
            file = open('acount_list.csv','w')
            fw=csv.writer(file)
            fw.writerows(rec)
            file.close()
            print('*'*30)

        if ch==3: 
            file = open('acount_list.csv','r')
            fr=csv.reader(file)
            acc_no=int(input('enter account no. :'))
            rec=[]

            for k in fr:
                if k[0]==acc_no:
                    acc_pr_no=int(input('enter primary mobile no. :'))
                    while True:
        
                        if str(acc_pr_no).isdigit() != True or len(str(acc_pr_no))>=8 or len(str(acc_pr_no))<=10 :
                                print('wrong number entered , please try again')
                                print()
                                acc_pr_no=int(input('enter primary mobile no. :'))
                                if str(acc_pr_no).isdigit() == True and len(str(acc_pr_no))>=8 and len(str(acc_pr_no))<=10:
                                    k[3]=acc_pr_no
                                    break
                        else:
                            k[3]=acc_pr_no
                            break
                    #secondary no.
                    acc_sd_no=int(input('enter secondary mobile no. :'))
                    while True:        
                        if str(acc_sd_no).isdigit() != True or len(str(acc_sd_no))>=8 or len(str(acc_sd_no))<=10 :
                            print('wrong number entered , please try again')
                            print()
                            acc_sd_no=int(input('enter secondary mobile no. :'))
                            if str(acc_sd_no).isdigit() == True and len(str(acc_sd_no))>=8 and len(str(acc_sd_no))<=10 :
                                k[4]=acc_sd_no
                                break
                        else:
                            k[4]=acc_sd_no
                            break
                    rec.append(k)
                else: rec.append(k)



            file.close()
            file = open('acount_list.csv','w')
            fw=csv.writer(file)
            fw.writerows(rec)
            file.close()
            print('*'*30)

        if ch==4:
            file = open('acount_list.csv','r')
            fr=csv.reader(file)
            acc_no=int(input('enter account no. :'))
            rec=[]
            for k in fr:
                if k[0]==acc_no :
                    c=0
                    for i in range(5):
                        acc_pass=int(input('enter old password :'))
                        if k[-1]==acc_pass:
                            new_acc_pass=int(input('enter new password :'))
                            while True:        
                                if str(acc_pass).isdigit() != True or len(str(acc_pass))>=5 or len(str(acc_pass))<=10 :
                                    print('wrong number entered , please try again')
                                    print()
                                    new_acc_pass=int(input('enter account password :'))
                                    if str(acc_pass).isdigit() == True and len(str(acc_pass))>=5 and len(str(acc_pass))<=10 :
                                        k[-1]=new_acc_pass
                                        break
                                else:
                                    k[-1]=new_acc_pass
                                    break
                            rec.append(k)
                        else:
                            print('wrong password entered,try again')
                            c+=1
                    if c==5:print('account has been blocked')
                else:rec.append(k)   
                
            file.close()
            file = open('acount_list.csv','w')
            fw=csv.writer(file)
            fw.writerows(rec)
            file.close()
            print('*'*30)

        if ch==0:
            print()
            break
 
def display_details():
    while True:
        print('*'*30)
        print('       DISLPAYING MENU      ')
        print('*'*30)
        print('1. Name ')
        print('2. Adress ')
        print('3. Numbers ')
        print('4. All Details')
        print('0. back...')
        print('*'*30)
        ch=int(input('enter your selection :'))
        print('*'*30)
        if ch==1:
            file = open('acount_list.csv','r')
            fr=csv.reader(file)
            acc_no=int(input('enter account no. :'))
            acc_pass=int(input('enter account pass :'))
            for k in fr:
                if k[0]==acc_no:
                    if k[-1]==acc_pass:
                        print(tabulate([['FIRST NAME',k[1][0]],['LAST NAME',k[1][1]]],headers='NAME'))
                        print('*'*30)
                        
                    else:
                        print('wrong password')
            file.close()
        if ch==2:
            file = open('acount_list.csv','r')
            fr=csv.reader(file)
            acc_no=int(input('enter account no. :'))
            acc_pass=int(input('enter account pass :'))
            for k in fr:
                if k[0]==acc_no:
                    if k[-1]==acc_pass:
                        print(tabulate([['CITY',k[2][0]],['AREA',k[2][1]],['BLOCK',k[2][2]],['BUILDING',k[2][3]],['HOUSE',k[2][4]]],headers='ADRESS'))
                        print('*'*30)
                    else:
                        print('wrong password')
            file.close()
        if ch==3:
            file = open('acount_list.csv','r')
            fr=csv.reader(file)
            acc_no=int(input('enter account no. :'))
            acc_pass=int(input('enter account pass :'))
            for k in fr:
                if k[0]==acc_no:
                    if k[-1]==acc_pass:
                        print(tabulate([['PRIMARY',k[3]],['SECONDARY',k[4]],['FAX',k[5]]],headers='NUMBERS'))
                        print('*'*30)
                    else:
                        print('wrong password')
            file.close()
        if ch==4:
            file = open('acount_list.csv','r')
            fr=csv.reader(file)
            acc_no=int(input('enter account no. :'))
            acc_pass=int(input('enter account pass :'))
            for k in fr:
                if k[0]==acc_no:
                    if k[-1]==acc_pass:
                        print(tabulate([['FIRST NAME',k[1][0]],['LAST NAME',k[1][1]],['CITY',k[2][0]],['AREA',k[2][1]],['BLOCK',k[2][2]],['BUILDING',k[2][3]],['HOUSE',k[2][4]],['PRIMARY',k[3]],['SECONDARY',k[4]],['FAX',k[5]],['BIRTH DATE',k[6]]],headers='NUMBERS'))
                        print('*'*30)
                    else:
                        print('wrong password')
            file.close()
        if ch==0:
            break

while True:
    print('*'*30)
    print('    welcome to Sethi bank   ')
    print('*'*30)
    print(str.strip('''
1. create a new account 
2. close my account
3. widraw money from atm 
4. deposit money to acount 
5. update account details 
6. view acount details
0. exit 
    '''))
    print('*'*30)
    ch=int(input('enter your selection :'))
    print('*'*30)
    print()
    print()
    if ch==1:create_acc()
    if ch==2:close_acc()
    if ch==3:money_withdraw()
    if ch==4:money_deposit()
    if ch==5:update_acc()   
    if ch==6:display_details()
    if ch==0:
        print('*'*30)
        print(' thanks for working with our bank')
        print('*'*30)
        break

