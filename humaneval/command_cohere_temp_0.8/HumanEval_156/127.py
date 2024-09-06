```python
def int_to_mini_roman(num):
    if num < 1000:        # Validate input is within range
        roman_num = []     # Initialize an empty list to store individual roman numerals
        for i in range(0, num + 1): # Loop runs till input number, plus one extra to include last iteration for value 1000
            roman_digit = []  # Initialize an empty list for each roman numeral digit
            if i == 1000:    # Handling value of 1000
                roman_digit = ['c', 'i', 'm']
            elif i == 500:    # Handling value of 500
                roman_digit = ['c', 'i', 'v']
            else:
                count = i
                while count > 0:
                    digit = str(count % 10) # Getting the last digit of the count
                    count = count // 10     # Keeping the remaining value by dividing by 10
                    roman_digit.append(digit) # Adding the last digit to the roman_digit list
                roman_digit.reverse()      # reversing the roman digit list to get the correct order
                if i == 1:               # Handling value of 1
                    roman_digit = ['i']    # Output should be 'i' instead of 'i'
                elif roman_digit[0] == '0': # If the first digit is 0, it's not valid
                    roman_digit = ['i']    # Output should be 'i' instead
            roman_num.extend(roman_digit) # Concatenating the roman numeral digits to the rom_num list
        return ''.join(roman_num)        # Joining the list elements into a string and returning the roman numeral
    else:
        return "Error!" + ": " + str(num) # If input is higher than 1000, return an error message
```

The script adheres to the problem's request to return the Roman numeral in lowercase. With input between 1 and 1000, the function iterates through each value, determining the particular Roman numeral representation before concatenating them into a string for the final output. The edge circumstances 500 and 1000 are addressed individually. When the input exceeds 1000, the function gives an error message.