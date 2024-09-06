```python
def choose_num(x, y):
    max_even = -1
    max_even_found = False
    
    for num in range(x, y + 1):
        if num % 2 == 0 and (max_even < num or max_even_found == False):
            max_even = num
            max_even_found = True
    
    return max_even if max_even_found else -1

# Test Cases
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(2, 3) == 2
```

This script defines a function `choose_num(x, y)` taking two parameters `x` and `y`, representing the lower and upper bounds of the range, respectively. The function searches for the largest even integer within this range, considering that the range is inclusive of both `x` and `y`. The variable `max_even_found` is used as a flag to track if an even number greater than `max_even` is found in the range. If no such even number is found, the function returns -1 to indicate the absence of such a number. The test cases confirm the correct behavior of the function.