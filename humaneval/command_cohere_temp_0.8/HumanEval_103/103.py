Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    total = (m + n) // 2
    count = m - n + 1
    if count == 0:
        return '-1'
    rounded_total = round(total)
    binary_representation = bin(rounded_total)[2:]
    return binary_representation if count > 0 else '-1'
```

The function `rounded_avg` calculates the average of the integers from `n` to `m`, considering the edge case where `n` is greater than `m`, in which case it returns `-1`. The answer is then rounded to the nearest integer, and the result is converted to binary. If the rounded average is zero (due to a count of 1), it will correctly return `-1` to account for the edge case described in the problem statement.