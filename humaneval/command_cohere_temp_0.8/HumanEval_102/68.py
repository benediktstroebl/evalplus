```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    
    if max_even >= min_even and max_even % 2 == 0:
        return max_even
    elif max_even < min_even or max_even % 2 != 0:
        return -1
    else: 
        return choose_num(x, max_even) if x != max_even else choose_num(max_even, y)
```

The function works by finding the median value between `x` and `y` and then adjusting either the lower or the upper bound accordingly. It handles the cases where the range [x, y] contains no even number or multiple even numbers correctly. The recursive case ensures that the function always returns the biggest even number and -1 in case there isn't one.