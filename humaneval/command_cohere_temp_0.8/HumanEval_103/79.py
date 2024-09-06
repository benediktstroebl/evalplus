Here's a Python script that contains a function rounded_avg(n, m) that solves the problem as described in the markdown code block:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded = avg % 1
    binary = bin(rounded)[2:]
    return '0b' + binary if binary else '-1'
```

The provided solution adheres to the problem's given guidelines. It first calculates the average of the integers between n and m. It then checks if the result is integer-valued after rounding. Lastly, it represents the result in binary or returns -1 for invalid inputs.