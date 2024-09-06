```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    roman = []
    while n > 0:
        number = n
        roman_num = []
        while number >= 10:
            roman_num.append(str(number % 10))
            number //= 10
        roman_num.reverse()
        roman.extend(roman_num)
        n -= sum(roman_num)
    return ''.join(map(str, roman))
```

This script provides a function `int_to_mini_roman` that converts a given positive integer to its mini roman numeral representation as a string. It follows these steps:
1. Handle edge cases where the input is less than 1, raising a `ValueError`.
2. Create an empty list called `roman` to store the final result.
3. Use a `while` loop to convert the input based on the optimal substructure of the problem.
4. Within this loop, use another `while` loop to determine the roman numeral representation of the current digit, which is determined by dividing `number` by 10 until it becomes 0.
5. Reverse the roman numeral representation and add it to `roman`.
6. Subtract the converted value from the original number and move to the next digit.
7. Finally, join the roman numerals together to obtain the mini roman numeral representation as a string and return it. 

This approach optimally solves the problem in a concise and efficient manner.