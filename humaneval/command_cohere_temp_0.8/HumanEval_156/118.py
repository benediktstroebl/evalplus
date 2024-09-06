```python
def int_to_mini_roman(num):
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_letters = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']

    result = []
    for i in range(len(roman_values)):
        while num >= roman_values[i]:
            num -= roman_values[i]
            result.append(roman_letters[i])

    return ''.join(result)
```

Let's break down the solution step by step:
1. We define the `roman_values` list, which contains the decimal equivalents of each Roman numeral from 'm' to 'i'.
2. Similarly, we define the `roman_letters` list, which contains the corresponding Roman letters.
3. We initialize an empty list called `result` to store the resultant Roman numeral.
4. We iterate through the `roman_values` list with a loop, similarly, we iterate through the `roman_letters` list.
5. Using a `while` loop, we repeatedly subtract the largest Roman numeral from the given number and append the corresponding Roman letter to the `result` list until the number is zero.
6. Finally, we join the elements of the `result` list into a single string and return the Roman numeral.

This approach leverages two loops and a `while` loop to efficiently convert the decimal number to its Roman numeral representation. The `result` list helps in keeping track of the Roman letters accrued during the conversion.