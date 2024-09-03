```python
def rounded_avg(n, m):
    """Computes the average of integers from n to m, rounds to nearest integer,
    converts to binary and returns the result or -1 if n > m.
    """
    if n > m:
        return -1
    avg = sum(range(n, m + 1)) / (m - n + 1)
    rounded = round(avg)
    binary = bin(rounded)[2:]
    return f"0b{binary}"
```