# This program is designed to show a transaction of a user on an automated teller machine(ATM) .

#   This are the pre-determined variables of the account at the login; 4 digit Pin: 1234
account_bal = 650
pre_pin = 1234

#   defining a function that would loop the entire process of each transaction

#   Setting the variables account_bal for the account balance and pin for the function when its loops through the
#   ATM transaction, because they are the only variable that have the tendency of changing after a transaction by the user


def main_menu(account_bal, pre_pin):
    r_main = input("Would you like to perform another transaction; Y/N? (Hint: Y: yes and N: no): ")
    if r_main == "Y" or r_main =="y":
        main(account_bal, pre_pin)
    elif r_main == "N" or r_main =="n":
        print("Thank you for banking with us, Have a nice day :)")
        print("CARD EJECTED()")
    else:
        print("You've made an invalid selection")


def main(account_bal, pre_pin):
    try:
        try:

            print()
            print("Welcome to the Bank of America automated teller machine\n\n")
            print("CARD INSERTED ()")
        #   pin authorisation (the 4 digit pin to access the card)

            pin = int(input("Please, enter your 4 digit pin: "))
            while pin != pre_pin:
                print("Pin code Declined")
                pin = int(input("kindly re-enter your 4 digit pin again: "))
            print()
            print("Pin-code Accepted!")
            print()
#   Display for the type of account type the user card is registered on
            print("What account type are you on;\n"
                  "1.   Checkings Account\n"
                  "2.   Savings Account\n"
                  "3.   Currents Account\n")
#   Look Up for account type through indexing
            acct_type = ["Checkings Account", "Savings Account", "Currents Account"]
            #   Input;
            acct_select = int(input("enter the specified number to the account type: "))
            #   Process;
            acct_select = acct_type[int(acct_select) - 1]
            #   Conditional statement on the selected account type the user selects
            #   This checkings account is the account the user is registered on.
            #       Therefore, it proceeds to the transaction menu
            if acct_select == "Checkings Account":
                print()
                print("WELCOME BACK!\nWhat kind of transaction would you like to perform?\n"
                      "1.   WITHDRAWAL\n"
                      "2.   CHECK ACCOUNT BALANCE\n"
                      "3.   MONEY TRANSFER\n"
                      "4.   CHANGE PIN CODE\n"
                      "5.   **ABORT OPERATION**\n")

            elif acct_select == "Savings Account":
                print("\nSorry, you are currently not registered under the account selected")
                main_menu(account_bal, pin)

            elif acct_select == "Currents Account":
                print("\nSorry, you are currently not registered under the account selected")
                main_menu(account_bal, pin)

            else:
                print("\nYou've made an invalid selection!")
                main_menu(account_bal, pin)

            print()
            transac_select = int(input("Kindly select the number specified for the transaction you want to perform: "))

            #   creating the lookup for the different transactions
            transac = ["WITHDRAWAL", "CHECK ACCOUNT BALANCE", "MONEY TRANSFER",
                       "CHANGE PIN CODE", "ABORT OPERATION"]
            #   Process; Getting the transaction the user chose by indexing
            transac_select = transac[int(transac_select) - 1]

            #   for the Withdrawal section
            if transac_select == "WITHDRAWAL":
                print("How much would you like to withdraw;\n"
                      "1.   $20\n"
                      "2.   $40\n"
                      "3.   $60\n"
                      "4.   $80\n"
                      "5.   $100\n"
                      "6.   others\n\n")
            #   From the options on withdrawal given above the user is to input the value from 1 - 6 to make withdrawal
            #   ...of their choice
                withdraw_select = int(input("Select the specified number of amount you want to withdraw: "))
                print()

                withdraw_opt = [20, 40, 60, 80, 100, "others"]

                withdraw_select = withdraw_opt[int(withdraw_select) - 1]

                #   Evaluating the amount withdraw from the account
                if withdraw_select == 20:
                    account_bal = account_bal - withdraw_select
                    print("TAKE YOUR CASH!\nThank you for banking with us;\n\nYour account balance is ${0:0.2f}".format(
                        account_bal))
                    main_menu(account_bal, pre_pin)

                elif withdraw_select == 40:
                    account_bal = account_bal - withdraw_select
                    print("TAKE YOUR CASH!\nThank you for banking with us;\n\nYour account balance is ${0:0.2f}".format(
                        account_bal))
                    main_menu(account_bal, pin)

                elif withdraw_select == 60:
                    account_bal = account_bal - withdraw_select
                    print("TAKE YOUR CASH!\nThank you for banking with us;\n\nYour account balance is ${0:0.2f}".format(
                        account_bal))
                    main_menu(account_bal, pin)

                elif withdraw_select == 80:
                    account_bal = account_bal - withdraw_select
                    print("TAKE YOUR CASH!\nThank you for banking with us;\n\nYour account balance is ${0:0.2f}".format(
                        account_bal))
                    main_menu(account_bal, pin)

                elif withdraw_select == 100:
                    account_bal = account_bal - withdraw_select
                    print("TAKE YOUR CASH!\nThank you for banking with us;\n\nYour account balance is ${0:0.2f}".format(
                        account_bal))
                    main_menu(account_bal, pin)

                elif withdraw_select == "others":
                    withdraw_select = int(input("Enter the amount you would like to withdraw: "))
                    account_bal = account_bal - withdraw_select
                    print("TAKE YOUR CASH!\nThank you for banking with us;\n\nYour account balance is ${0:0.2f}".format(
                        account_bal))
                    main_menu(account_bal, pin)

                elif withdraw_select > account_bal:
                    print("You do not have sufficient funds!")
                    main_menu(account_bal, pin)

                else:
                    print("You've made an invalid selection")
                    main_menu(account_bal, pin)


#   Checking of the account balance section
            elif transac_select == "CHECK ACCOUNT BALANCE":
                print()
                print("YOUR ACCOUNT BALANCE IS; ${0:0.2f}".format(account_bal))
                main_menu(account_bal, pin)


#   Money Transfer section
            elif transac_select == "MONEY TRANSFER":
                print()
                print("MONEY TRANSFER\nThis service you are requesting is currently not available")
                main_menu(account_bal, pin)


#   Changing of the pin code section
            elif transac_select == "CHANGE PIN CODE":
                print()
                print("CHANGE PIN CODE")
                pre_pin = pin
                pre_pin = int(input("Enter the 4 digit pin you are currently using: "))
                while pre_pin != pin:
                    print("You've entered a wrong pin")
                    pre_pin = int(input("Re-enter the 4 digit of your pin again: "))
                else:
                    pin = int(input("Enter your new 4 digit pin: "))
                    while len(str(len)) != 4:
                        print("INVALID!!! You have to enter a 4 digit pin")
                        pin = int(input("Enter your new 4 digit pin again: "))
                    else:
                        print()
                        print("Your new pin is; ", pin)
                        print()
                    main_menu(account_bal, pin)


#   Aborting the ATM operation
            elif transac_select == "ABORT OPERATION":
                print()
                print("Thank you for banking with us. :)")
                print("CARD EJECTED()")



            else:
                print("You've made an invalid selection")

        except ValueError:
            print("You made an invalid input")
            main_menu(account_bal, pre_pin)

    except IndexError:
        print("You've made an invalid input")
        main_menu(account_bal, pre_pin)


main(account_bal, pre_pin)
