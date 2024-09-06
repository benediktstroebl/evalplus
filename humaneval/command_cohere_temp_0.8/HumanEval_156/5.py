```python
def int_to_mini_roman(num):
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_digits = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    result = []
    for i in range(len(roman_values)):
        while num >= roman_values[i]:
            result.append(roman_digits[i])
            num -= roman_values[i]
    return ''.join(result)
```

The `int_to_mini_roman` function takes a single argument, `num`, which is the number to be converted to its roman numeral equivalent. It uses two arrays, `roman_values` and `roman_digits`, to store the corresponding roman numeral values and digits.

The function starts by initializing an empty list called `result` to store the roman digits corresponding to the decimal value of the input number. It then loops through the length of `roman_values`, which stores the largest decimal value that each roman digit can represent.

Within this loop, the function checks if the current roman digit can be used to represent a value equal to or less than the remaining value of `num`. If it can, it adds the roman digit to the result list and subtracts its corresponding value from `num`. The loop continues until all the value of `num` has been converted into roman digits.

Finally, the function joins the result list into a single string and returns it, representing the roman numeral equivalent of the input number.  This solution is efficient as it uses two arrays for lookup and doesn't require any recursive or iterative methods, making it O(n), where n is the given integer input.