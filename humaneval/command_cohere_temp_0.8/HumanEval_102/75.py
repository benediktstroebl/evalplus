```python
def choose_num(x, y):
    max_even = max(x, y)
    floor_even = max_even - 1
    if floor_even % 2 == 0:
        return floor_even
    else:
        return -1
```

The function `choose_num()` takes two positive numbers `x` and `y` as arguments and returns the biggest even integer that falls in the range `[x, y]`. If no such even number exists within this range, it returns -1. 

Here's how the function works:
1. Start with the maximum of `x` and `y` and call it `max_even`. 
2. Deduct 1 from `max_even` to get the highest possible even number that is still within the range. This number is called `floor_even`. 
3. Check if `floor_even` is an even number. If it is, return it. If not, nothing in the range is even, so return -1. 

This algorithm efficiently identifies the tallest even number in the range without explicit looping or explicit integer checking, making it a sleek 'one-liner' solution.