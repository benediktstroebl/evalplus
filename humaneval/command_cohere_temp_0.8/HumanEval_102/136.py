```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even & 1
    return max_even if max_even <= max(x, y) else -1
```

The function `choose_num()` takes two integers `x` and `y` as parameters. It first calculates the middle value of the range [x, y] as `((x + y) // 2)` and then increments it by one if it's odd to make it the biggest even value in the range. If this value is larger than either `x` or `y`, it means there is no biggest even integer in the range, so the function returns -1. 

The logic leverages the fact that the average of two integers is always even, and if the range includes odd numbers, the biggest value will still be the one rounded down from the average.