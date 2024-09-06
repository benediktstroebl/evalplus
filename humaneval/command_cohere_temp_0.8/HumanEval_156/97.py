```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n < 1000:
        result = []
        for x in range(1, n + 1):
            if x == 5:
                result.append('v')
            elif x == 10:
                result.append('x')
            elif x == 25:
                result.append('xx')
            elif x == 50:
                result.append('l')
            elif x == 100:
                result.append('c')
            elif x == 250:
                result.append('cc')
            elif x == 500:
                result.append('d')
            elif x == 750:
                result.append('dc')
            elif x == 900:
                result.append('x')
            else:
                result.append(str(x))
        return ''.join(result)
    else:
        raise ValueError("Input must be between 1 and 1000")
```

This code defines the `int_to_mini_roman` function, which accepts a positive integer as input and returns the lowercase roman numeral equivalent if it's within the range of 1 to 1000. It utilizes nested conditional statements to iterate through each digit of the input number, converting it to its roman numeral form. If the input is greater than 1000 or non-positive, it raises a `ValueError` with an appropriate error message.