```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y + 1) if z % 2 == 0), default=-1)
    return max_even
```

The code uses a generator expression with a range and a filter based on the modulo operation to find the biggest even number in the range [x, y] inclusive. The `default=-1` argument of the max function is used to handle the case where no even number is found in the range, which would otherwise raise a `ValueError` exception. 

To test this script, you can call the `choose_num()` function with a variety of cases and compare it with the provided examples in the original problem description.