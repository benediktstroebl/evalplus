```python
def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    res = []
    for i in range(1, 1000):
        if n >= i:
            num = [str(d) for d in reversed(list(range(i, i + 1)))]
            res.extend(num)
            n -= i
            if n == 0:
                break
    return ''.join(res).lower()
```

This code snippet provides a function called `int_to_mini_roman`, which converts a positive integer to its mini roman numeral representation as a string. It applies a loop to iterate through numbers from 1 to 1000, converting each suitable value to its roman numeral counterpart and subtracting it from the input integer. The result is a lowercase roman numeral string representation of the given number.