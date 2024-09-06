```python
def choose_num(x, y):
    max_even = -1
    temp = x
    while temp <= y:
        if temp % 2 == 0:
            max_even = temp
        temp += 1
    return max_even
```

The function `choose_num()` takes two parameters, `x` and `y`, and searches for the biggest even integer that lies in the range `[x, y]`. It does so by initializing `max_even` to the value `-1` and then iteratively moving through the range from `x` to `y` (inclusive) checking if each number is even. If a number is even, it updates `max_even` to that number. Once the loop is done, the function returns `max_even`. 

The following test cases pass with this implementation:
```python
>>> choose_num(12, 15)
14
>>> choose_num(13, 12)
-1
```

This solution is efficient because it only iterates through the range once, making it a linear time solution.