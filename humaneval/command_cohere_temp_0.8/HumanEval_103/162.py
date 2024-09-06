Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded = avg % 1
    binary = bin(rounded)[2:]
    return '0b' + binary if binary else '0b0'
```

The script provides a function that:
- Calculates the average of numbers from `n` to `m` and rounds it to the nearest integer.
- Checks if `n` is greater than `m`, and returns `-1` if it is.
- Converts the rounded integer to binary.

The function is designed to be self-contained and easy to use, following the problem statement's guidelines. It can be imported as a standalone function into other Python scripts or run directly for testing.