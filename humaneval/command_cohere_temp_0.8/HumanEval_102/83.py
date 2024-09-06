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

The function `choose_num()` takes two parameters, `x` and `y`, and searches for the biggest even integer that exists in the range between them. It does so by initializing `max_even` to -1 and then iterating through numbers starting from `x` and ending with `y`, checking if each number is even. If it finds a valid even number, it updates `max_even` to that number. The loop terminates when the next iteration would go beyond the range [x, y], ensuring that all eligible even numbers are considered. The function returns the value of `max_even` if it exists; otherwise, it returns -1. 

This approach guarantees that the function considers all possible even numbers within the specified range and selects the largest one.