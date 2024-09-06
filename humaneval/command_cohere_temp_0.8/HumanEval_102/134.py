```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    
    if max_even >= min_even and max_even % 2 == 0:
        return max_even
    elif max_even < min_even or max_even % 2 != 0:
        return -1
    else:
        return -1
```

The Python script defines a function choose_num, which takes two positive numbers x and y as input and returns the biggest even integer that falls within the range of [x, y], or -1 if no such number exists. 

The function first calculates the midpoint between x and y, named max_even, and the minimum even number within the range, named min_even. If max_even is both greater than or equal to min_even and is also an even number, it returns max_even as the solution. Otherwise, the function returns -1, indicating that no suitable even number can be found within the range. 

This approach efficiently determines the solution and handles the conditions outlined in the prompt.