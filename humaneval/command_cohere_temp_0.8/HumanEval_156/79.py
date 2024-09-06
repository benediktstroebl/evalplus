```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1000):
        if n >= i:
            num = [str(j) for j in reversed(list(range(i, i + 1)))]
            res += [next(d for d in num if d != '0')]
            n -= i
    return ''.join(res)
```

This code snippet above provides a Python function int_to_mini_roman that takes a positive integer as input and returns its corresponding roman numeral in lowercase as a string. It validates the input being greater than 0 before iterating through the range from 1 to 1000. It accumulates roman numerals corresponding to the value of the input in reverse order and converts them into a string, ensuring that no leading 0s are included in the roman numeral.