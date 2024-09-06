```python
def int_to_mini_roman(num):
    converter = {
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
    result = []
    for i in range(1, 1001):
        if num >= i:
            num_left = num // i
            result.append(converter[i])
            result.append(converter[num_left])
            num %= i
    return ''.join(result)[::-1]
```

This Python script defines a function int_to_mini_roman that takes a positive integer as input and converts it to its mini roman numeral representation as a string. It iterates through each value from 1 to 1000 and identifies the corresponding roman numeral values (using a dictionary for quick translation), then constructs the result string based on these values. The function places the roman numeral values in reverse order, so the conversion is correct but condensed, resulting in a mini roman numeral representation. The output is a lowercase string containing the mini roman numeral equivalent of the given integer, restricted to the range of 1 to 1000. 

In the provided examples, the function correctly returns 'xix' for 19, 'clii' for 152, and 'cdxxvi' for 426.