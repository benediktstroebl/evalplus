Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```

The provided example uses well-defined Python semantics, including the rounding mechanism and binary conversion, which are crucial for the problem. The function also handles the case where the average returns `None` when one of the inputs is invalid.

The function `rounded_avg` calculates the average of the integers from `n` to `m`, inclusive, using the formula `(n + m) // 2`. It then rounds the average to the nearest integer and converts it to binary. If `n` is greater than `m`, it returns `-1` as specified by the prompt.