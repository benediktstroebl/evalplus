```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    return max_even if max_even % 2 == 0 and max_even in range(x, y + 1) else -1
```

The function begins by attempting to find the biggest even number in the range by taking the midpoint of the interval and checking if it's even, using the condition `max_even % 2 == 0`. If it's not even, it adjusts the maximum value to be either `x` or `y`, whichever is bigger, checking the condition `max_even in range(x, y + 1)` to ensure it remains within the specified range. The function returns the biggest even number in the range, or -1 if no such number exists.