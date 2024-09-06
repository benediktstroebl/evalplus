```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    return max_even if max_even % 2 == 0 and max_even in range(x, y + 1) else -1
```

The function first tries to find the biggest even integer in the range [x, y] by taking the midpoint of the range (`(x + y) // 2`) and checking if it is even and within the range. It then compares this value to the maximum of either `x` or `y` (whichever is bigger) and returns it if it's valid. If this doesn't yield a valid result, the function returns -1.