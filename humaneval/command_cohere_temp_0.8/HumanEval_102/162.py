```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y + 1) if z % 2 == 0), default=-1)
    return max_even
```

The code uses a generator expression with a range and a filter based on the modulo operation (z for z in range(x, y + 1) if z % 2 == 0) to find the biggest even number in the range [x, y] inclusive. The `max()` function is then applied to this generator expression, with a default value of -1 in case no even number is found in the range. 

This ensures that the biggest even number within the range is found and returned, or a -1 is returned if no even number is found within the range. 

To handle edge cases where the range is empty or doesn't contain any even numbers, the function relies on Python's `max()` functionality to return the default value (-1 in this case) when no even number is found. 

The function should be able to handle cases where both x and y are even as well as where x and y are odd, and also cases where x is odd and y is even, etc. 

This is ensured by the even filter in the generator expression.