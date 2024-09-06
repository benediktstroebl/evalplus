```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y + 1) if z % 2 == 0), default=-1)
    return max_even
```

The code uses a generator expression with a range and a filter based on the modulus operation to find the biggest even integer in the range [x, y] inclusive. The `default=-1` argument of the max function sets the value to return when no even integer is found in the range, making the function conform to the test cases where no biggest even number exists.