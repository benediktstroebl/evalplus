```python
def int_to_mini_roman(num):
    if num < 1000:
        roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_digits = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
        result = []
        for i in range(len(roman_values)):
            while num >= roman_values[i]:
                result.append(roman_digits[i])
                num -= roman_values[i]
        return ''.join(result)
    else:
        return "Error! Number must be between 1 and 1000."
``` 

In the code above, we iterate through each digit of the number and subtract the corresponding Roman numeral value, accordingly, finally, joining the Roman digits to form the answer. We also include a condition to check if the input number is greater than 1000 to handle invalid inputs and return an appropriate error message.