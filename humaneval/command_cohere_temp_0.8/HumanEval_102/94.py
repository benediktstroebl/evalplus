```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    
    if max_even % 2 == 0 and max_even >= x and max_even <= y:
        return max_even
    else:
        return -1

# Tests:
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(4, 10) == 6
assert choose_num(10, 4) == -1
```

This Python script defines a function `choose_num(x, y)` designed to find the largest even integer within the inclusive range between two positive numbers `x` and `y`. The function first calculates the average of `x` and `y` and then compares it to both `x` and `y` to ensure it selects the largest even number. If no even number exists within the range, it returns -1. The script includes tests to validate the function's behavior against specific cases.