```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Convert number to list of digits and reverse it to avoid incorrect leading values
    digits = [int(d) for d in str(n)[::-1]]
    
    result = []
    for i in range(len(digits)):
        digit = digits[i]
        if digit < 5: 
            result.append(str(digit))
        else:
            result.append('x')
            digit -= 5
            result.append(chr(ord('a') + digit))
            
    return ''.join(result).lower()
```

Let's break down the solution step by step:
1. **Input Validation**: The function starts by checking if the input number is less than 1. If this is the case, it raises a `ValueError`, ensuring that only positive integers are accepted.
2. **Reverse the digits**: The number is converted into a list of digits and then reversed. This reversal is intentional and helps us avoid incorrect leading values in the Roman numeral. For example, the number 8 would translate to VIII, not IV.
3. **Iterative Conversion**: The function then iterates over each digit, starting from the last digit (the ones place) and moving towards the ones place. This is crucial because it ensures that we correctly convert the highest place value first.
4. **Handling Digits Less Than Five**: When a digit less than five is encountered, it's directly added to the result string as is, without any modification.
5. **Handling Digits Greater Than or Equal To Five**: If a digit is greater than or equal to five, it's converted to a lowercase letter ('a' to 'e') by subtracting five and using the corresponding ASCII code. This forms the mini Roman numerals.
6. **Build the Final Result**: The function constructs the final Roman numeral string by joining the list of result elements together.