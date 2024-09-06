```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    
    if max_even == min_even or max_even % 2 == 0:
        return max_even
    
    return -1
```

The Python script defines a function `choose_num` taking two positive numbers `x` and `y`, returning the biggest even integer in the range `[x, y]` or `-1` if no such number exists. The function assesses the midpoint between `x` and `y` (including both in the range). If the midpoint is equal to the lowest even integer within the range or is even itself, it returns the midpoint. Otherwise, it returns `-1` since no bigger even number exists in the given range. 

This approach efficiently solves the problem while maintaining a clear and readable code structure.