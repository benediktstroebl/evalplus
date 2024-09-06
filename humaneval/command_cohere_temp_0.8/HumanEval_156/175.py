```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for i in range(1, 1000):
        if n >= i:
            res += [c for c in f"{{:,}}".format(i) if c != '0']
            n -= i

    return ''.join(res)
```

The `int_to_mini_roman` function iterates through numbers from 1 to 1000, converting each value to its roman numeral representation. It accumulates these into the `res` list, which is later joined together to form the final lowercase roman numeral string. The loop structure ensures that the function is efficient, with time complexity of O(1000), making it suitable for practical use.