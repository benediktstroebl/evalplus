```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2

    if max_even == min_even or max_even % 2 == 0:
        return max_even
    else:
        return -1
```

The function `choose_num()` takes two positive numbers `x` and `y` as arguments and returns the biggest even integer that falls in the range `[x, y]`, or `-1` if no such number exists.

It works by finding the midpoint between `x` and `y` and checking if it's an even integer. If the midpoint is even, it returns the midpoint. If the midpoint isn't even, it checks if the maximum possible even number in the range is equal to the midpoint or closer to `x`. If it is, it returns the maximum even number; otherwise, it returns `-1`.