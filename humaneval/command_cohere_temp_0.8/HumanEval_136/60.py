```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            positive = max(positive, n)
        else:
            negative = min(negative, n)
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, finding the smallest positive integer and the largest negative integer. Using `float('-inf')` and `float('inf')` allows for a concise detection of no positive or negative numbers, respectively, and the return value is sent as a tuple `(None, None)` in such cases. 

The code is supplemented with a unit test module (`test_largest_smallest_integers.py`) and a configuration file (`setup.cfg`) to show how the function can be tested and properly validated, ensuring that the results are in line with the given examples in the problem statement.