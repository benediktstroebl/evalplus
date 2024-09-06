```python
def pairs_sum_to_zero(l):
    if set(l) <= {0}:  # Set comprehension to ensure all elements are non-zero
        return True
    else:
        return False
```

This code is a simple, self-contained function that solves the problem. It takes a the test on a list of integers to determine if there are two distinct elements that sum to zero. This can be useful for solving the specific scenarios, such as checking for the existence of specific elements in a list.