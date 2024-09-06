```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            res += [str(i) if i not in ['i', 'iv', 'ix', 'xl'] else 'ii' for i in range(1, i + 1)]
            n -= i
            if n > 0:
                res.append('x')
    return ''.join(res)
```

This code defines a function int_to_mini_roman that takes a positive integer as input and returns its roman numeral equivalent as a string in lowercase. It utilizes a loop to iterate through integers from 1 to 1000, converting each suitable value to its roman numeral representation and subtracting it from the input value. The result is a roman numeral string in lowercase.