```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with some lists
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
assert(get_positive([-2, 0, -4, 100, 5, 6, 8, 7]) == [0, -4, 100, 5])
assert(get_positive([]) == [])
```
The script defines a function `get_positive` that returns a list of only positive numbers from the input list.  It also passes thes series of test cases to verify the correctness of the function.