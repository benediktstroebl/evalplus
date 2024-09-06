Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) // 2
    return bin(round(avg))[2:]
```
This function takes two integers `n` and `m` as input and returns the binary representation of the rounded average of the integers between them.

The function first checks if `n` is greater than `m`, and since this condition is not met in the problem statement's examples, it returns `-1` for this case for now. Next, it computes the average of `n` and `m` by adding their values and dividing by 2. The result is then rounded to the nearest integer, and its binary representation is returned.