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

The function `choose_num()` takes two arguments `x` and `y` that represent the range for the search. The function then iterates through the range and checks if the current number is even. If it is even and greater than the current `max_even` value, it updates the `max_even` value. The function returns `-1` if no even number is found in the range. 

This code solves the problem using a simple iterative method and will return the desired even number if it exists in the range or `-1` otherwise. 

This approach has a time complexity of O(m) where m is the difference between `x` and `y`.