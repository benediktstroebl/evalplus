```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    
    if max_even % 2 == 0 and max_even <= max(x, y):
        return max_even
    else:
        return -1
```

The algorithm aims to find the biggest even integer between two given numbers `x` and `y`. It starts by finding the midpoint between `x` and `y` (`(x + y) // 2`) and then updates `max_even` to be equal to the largest of the following:
- The midpoint.
- The value of `x`.
- The value of `y`.

This ensures that `max_even` represents the largest even integer in the given range. Then, the algorithm checks if `max_even` is both even and within the range `[x, y]` (exclusive). If it passes both conditions, it returns `max_even`; otherwise, it returns `-1` as there are no even numbers in the range. 

The approach takes advantage of the fact that the largest even number in the range will always be either the midpoint or one of the two endpoints.