Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    if n > m:
        return -1
    while m - n > 1:
        if m >= n:
            digits = len(str(m))
        else:
            digits = len(str(n))
        if 2 ** (digits - 1) <= total:
            count += 1
        elif 2 ** digits <= total:
            count -= 1
        m //= 2
        n //= 2
        total //= 2
    if m == n:
        if m == 0:
            return '0b0'
        elif m == 1:
            return '0b1'
        else:
            return f'0b{count}'
    else:
        return '-1'
```

This code provides a solution to the described problem. It follows a nuanced process to determine the average and the binary representation, accounting for overlapping ranges and handling edge cases. The `rounded_avg` function ultimately returns the binary representation of the average or -1 if the range is invalid.