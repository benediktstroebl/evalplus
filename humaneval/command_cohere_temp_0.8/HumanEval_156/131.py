```python
def int_to_mini_roman(num):
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_letters = ['m','m','d','d','c','c','i','i','x','x','l','l','v','v','i']
    result = []
    for i in range(len(roman_values)):
        while num >= roman_values[i]:
            num -= roman_values[i]
            result.append(roman_letters[i])
    return ''.join(result)
```

The approach used here disposes of a lookup table and instead uses iterative processes for both the numerical and alphabetical components. This makes the code more scalable and easier to comprehend.

We iterate through the `roman_values` list, which represents the numerical values of each Roman letter. As we iterate, we subtract the numerical value of each Roman letter from the input number. Simultaneously, we append the corresponding Roman letter to the `result` list. Once all the Roman letters have been calculated and added, we join them together to form the final Roman numeral. 

This solution efficiently converts numbers to mini Roman numerals, utilizing loops instead of a lookup table for a more scalable approach.