```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y + 1) if z % 2 == 0), default=-1)
    return max_even
```

The code uses a generator expression with a range and a filter based on the modulo check of even numbers to find the biggest even number in the range `[x, y]` inclusive. The `default=-1` argument of the max function sets the value to -1 if no even number is found in the range, hence solving the problem. 

To handle the edge case where both `x` and `y` are even, the function could be modified to swap the biggest even number with the closest smaller even number if it equals `y`. This modification ensures that the function always returns the biggest even number and is only relevant when both `x` and `y` are even. 

To handle the edge case where both `x` and `y` are odd, the function could be modified to return the biggest odd number in the range. However, since the provided `choose_num` function is specified to return the biggest even number, the odd case consideration is out of its scope.