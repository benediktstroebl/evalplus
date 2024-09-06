```python
def choose_num(x, y):
    max_even = -1
    target = y
    while target > x:
        if target % 2 == 0 and target not in (x, y):
            max_even = target
        target -= 2
    return max_even
```

The function iterates through numbers starting from `y` by descending in an increment of 2, checking if the number is even and not equal to `x` or `y`, and if so, updates `max_even`. The loop terminates when it hits the value of `x` or goes below it, ensuring it covers the entire range. The logic efficiently identifies the largest even integer within the range without unnecessary checks.