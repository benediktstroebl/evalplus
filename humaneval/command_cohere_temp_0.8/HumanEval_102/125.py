```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    
    if max_even == min_even or max_even % 2 == 0:
        return max_even
    elif max_even > min_even:
        return -1
    else:
        return min_even
```

The function `choose_num()` takes two positive numbers `x` and `y` as arguments and returns the biggest even integer that falls in the range `[x, y]`, or `-1` if no such number exists.

This is achieved by defining the variable `max_even` as half of the sum of `x` and `y`, and `min_even` as the maximum of `x` and `y` divided by 2. If the midpoint is even, or if it's equal to the minimum even number in the range, it's returned. If the maximum number in the range is bigger than the minimum, `-1` is returned, as there are no even numbers in the range. Otherwise, the minimum even number is returned. 

**NOTE:** This solution assumes that the given numbers `x` and `y` are both positive and may need adjustments for invalid inputs.