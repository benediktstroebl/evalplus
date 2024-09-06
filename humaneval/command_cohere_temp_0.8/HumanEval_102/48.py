```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    
    if max_even % 2 == 0 and max_even >= x and max_even <= y:
        return max_even
    else:
        return -1
```

The algorithm aims to find the biggest even integer within the range [x, y]. It starts by calculating the midpoint between x and y, rounding up if it's not an integer, and then comparing this value to both x and y to ensure it's the largest even number within the specified range. If no such even number exists, it returns -1.