# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours (This program)
# Rewrite your pay program using 'try' and 'except' so that your program handles non-numeric input and re-prompts for another value

print("Now that you've worked at our company, please state your pay and we will evaluate how well you need to be compensated!")
Hours = int(input('Hours Worked: '))                                                                                                # Takes the input for hours and converts it to an integer
PPHour = float(input('Money per hour: '))                                                                                   # Takes input for Money gained per hour and converts it to a float
                                                                                                                                    

if Hours >= 40:                                                                                                                  # Checks if Hours worked is above 40
        pay = (PPHour*1.5)                                                                                                        # Takes pay per hour and multiplies it by 1.5
        Compensation = ('Gross pay: ${}').format(pay)                                                                               # Formats the variable 'pay' into the string
        print('Congratulations! The company deems you worthy of further compensation, your pay has been raised by 1.5 times!')              # Flavour text
        print(Compensation)                                                                                                             # Prints resultant compensation
else:
    print('Unfortunately our company deems you incapable of further compensation, try harder next time!')               # If hours worked is not above 40 then a discouraging message appears
    print(PPHour)                                                                                                       # Prints input from the pay per hour message

input('-Press Any Key to Exit Program-')                # Prevents program from closing until key is pressed