Here's a Python script with a self-contained function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    total = (n + m) // 2
    count = m - n + 1
    avg = total // count
    return bin(round(avg))[2:]
```

The provided Python script solves the problem using the midpoint of the range of numbers. It first checks if the count of numbers in the range is invalid (fewer than two) and returns -1 if so. Otherwise, it calculates the average of the elements in the range and rounds it to the nearest integer. Finally, it converts the rounded average to binary and returns the result.