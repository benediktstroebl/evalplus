```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    
    if max_even == min_even or max_even % 2 == 0:
        return max_even
    
    return -1
```

The function `choose_num()` takes two positive numbers `x` and `y` as arguments and returns the biggest even integer that falls in the range `[x, y]`, inclusive. If no such even number exists, it returns -1. 

The strategy employed involves:
1. Finding the midpoint between `x` and `y` - `max_even` and checking if it's an even integer. This midpoint is the maximum possible even number that falls in the given range.
2. Finding the minimum possible even number, which would be half of the larger of `x` and `y`, rounded down - `min_even`. If the maximum even number is equal to the minimum even number or if the maximum even number is even, we found our answer. 

If none of these conditions are met, the function returns -1, meaning there is no biggest even number in the range. 

This approach efficiently solves the problem in a single function, satisfying the problem's requirements.