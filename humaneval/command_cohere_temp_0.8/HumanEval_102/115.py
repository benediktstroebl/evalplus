```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even & 1
    return max_even if max_even <= max(x, y) else -1
```

The function starts by finding the mathematical middle point between `x` and `y` and then adjusts this middle point to be the biggest even integer in that range by adding `1` if the middle point is odd. The function returns this value if it is less than or equal to the maximum of `x` and `y`, and -1 otherwise. This is done to accommodate the fact that the specified range needs to be inclusive of both `x` and `y`, but the middle point cannot be odd if it is to be the biggest even integer in the range. Thus, the middle point is adjusted to the next even number up, if needed, to find the biggest even integer in the range.