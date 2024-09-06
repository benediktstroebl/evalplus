```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function with some lists
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
assert(get_positive([-2, 0, -5, -20]) == [-2, 0, -5])
assert(get_positive([5, -6]) == [5, -6])

``` 
This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. The test cases verify that function's correctness by passing different lists and checking if the returned lists contain only the expected positive numbers.