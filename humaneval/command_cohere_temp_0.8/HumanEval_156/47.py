```python
def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    res = []
    for i in range(1, 1000):
        if n >= i:
            num = [str(j) for j in range(i, 0, -1)]
            res.extend(num)
            n -= i
    
    return ''.join(res)
```

The core idea is to iterate through numbers from 1 to 1000 and accumulate the roman numeral representation as we go. The test cases provided illustrate how the function behaves for various inputs.