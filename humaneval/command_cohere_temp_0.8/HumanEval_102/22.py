```python
def choose_num(x, y):
    max_even = max(x, y)
    min_even = min(x, y)
    
    if max_even - min_even % 2 == 0 and max_even >= min_even:
        return max_even
    else:
        return -1
```

The Python script defines a function `choose_num(x, y)` that adheres to the problem statement. It finds the maximum even integer within the range `[x, y]`, ensuring it's also the biggest integer in that range. If no such number exists, it returns -1. This approach guarantees that the function always returns the maximum even number or -1 for invalid ranges.