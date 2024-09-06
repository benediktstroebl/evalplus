```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even % 2  # Make it inclusive
    if max_even >= x and max_even <= y:
        return max_even
    else:
        return -1
```

The function `choose_num()` takes two positive numbers `x` and `y` as arguments and returns the biggest even integer that falls in the range `[x, y]`, or `-1` if no such number exists.

It calculates the midpoint between `x` and `y` and then increments it by 1 to ensure that the midpoint is the biggest even number in the range. Then it checks if this midpoint integer is within the range `[x, y]`. If it is, it returns this even integer; otherwise, it returns `-1`. 

This approach ensures an efficient and concise solution.