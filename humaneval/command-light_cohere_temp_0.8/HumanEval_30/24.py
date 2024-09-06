```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

# Test case 2
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]

# Test case 3
assert len(get_positive([-100, 2, -5, -30])) == 3

# Test case 4
assert len(get_positive([1, 2, 3, -1, 4])) == 4
``` 
The code defines a function `get_positive` that takes an input list and returns a new list containing only the positive numbers from the input list. The test cases are used to verify the correctness of the function by passing various input lists and asserting that the returned list contains only the positive numbers.