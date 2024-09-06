```python
def get_positive(input_list):
    """Return only positive numbers in the list"""
    return [num for num in input_list if num > 0]

# Unit tests
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
expected = [5, 3, 2, 3, 9, 123, 1]
got = get_positive(input_list)
assert len(got) == len(expected), "Test failed: Lists lengths do not match"
assert got == expected, "Test failed: List values do not match"

# Another test with a different list
input_list2 = [-1, 2, -4, 5, 6]
expected2 = [2, 5, 6]
got2 = get_positive(input_list2)
assert got2 == expected2, "Test failed: List values do not match"
```
This script defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers. The unit tests verify that correctness of the function by checking if the returned list matches the expected list for various input lists.