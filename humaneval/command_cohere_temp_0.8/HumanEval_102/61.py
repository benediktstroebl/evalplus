```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    
    if max_even % 2 == 0 and x <= max_even <= y:
        return max_even
    else:
        return -1
```

The function starts by finding the midpoint between `x` and `y` and checks if it's even. If it's not even, it will then check if `x` is even and replace the midpoint with the maximum of either `x` or the midpoint. It will then do the same with `y`. This ensures that the maximum even integer between `x` and `y` is found, and if it's not possible, it returns -1.