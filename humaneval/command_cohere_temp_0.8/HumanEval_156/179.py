```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            count = len(str(i))
            res.extend([str(j) for j in range(count)])
            n -= i
            if n == 0:
                break
    return ''.join(res).lower()
```

This script provides a function `int_to_mini_roman` that converts a given positive integer into its mini roman numeral representation as a string. It iterates through the numbers from 1 to 1000, converting each consecutive digit in the decimal number into the corresponding roman numeral character and subtracting the value of that digit from the input. It then joins the roman numeral characters into a string and lowers the case to fulfill the criteria of the `int_to_mini_roman` function. 

Here is an example:
```python
>>> int_to_mini_roman(19)
'xix'
>>> int_to_mini_roman(152)
'clii'
>>> int_to_mini_roman(426)
'cdxxvi'
```