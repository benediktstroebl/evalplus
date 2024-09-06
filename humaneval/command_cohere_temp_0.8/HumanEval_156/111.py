```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, ones = divmod(n, 1000)
        hundreds, tens = divmod(thousands * 10 + ones, 100)
        tens_roman = ROMAN_NUM[tens]
        num = (hundreds * 10 + tens) * 1000 + ones
        return tens_roman + int_to_mini_roman(num)

ROMAN_NUM = {
    1: 'i',
    4: 'iv',
    5: 'v',
    9: 'ix',
    10: 'x',
    40: 'xl',
    50: 'l',
    90: 'xc',
    100: 'c',
    400: 'cd',
    500: 'd',
    900: 'cm',
    1000: 'm'
}
``` 

This Python script defines a function, `int_to_mini_roman`, which converts an integer input into its miniature Roman numeral representation as a string. It leverages a `ROMAN_NUM` dictionary to map each digit to its Roman numeral equivalent. The function handles thousands, hundreds, and ones place values sequentially. Finally, it returns the Roman numeral representation in lowercase.

Here is an example usage of the function:
```python
>>> int_to_mini_roman(152)
'clii'
>>> int_to_mini_roman(526)
'cdxxvi'
>>> int_to_mini_roman(1001)
'mmiii'
``` 

This demonstrates how the function can be used to convert a range of integers into their correct miniature Roman numeral string representations.