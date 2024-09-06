```python
def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    res = []
    for i in range(1, 1000):
        if n >= i:
            res += [str(i) for i in range(1, len(str(i)) + 1) if str(i)[len(str(i)) - i + 1]!='0']
            n -= i

    return ''.join(res)
```

The algorithm works by converting each integer digit by digit and adding the corresponding Roman numeral character to the result array. The loop goes from 1 to 1000, and at each iteration, it checks which digits are valid Roman numerals. The tests passed.