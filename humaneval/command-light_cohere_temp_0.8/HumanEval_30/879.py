```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function
test_positive = get_positive([1, 2, 3, 4, 5, 6, 7])
assert len(test_positive) == 6
assert all(test_positive >= 0)

# Test passing lists with both positive and negative numbers
test_passing = [[-1, 2, 3, 4, 5], [1, 2, -3, 5, 6])
assert len(get_positive(test_passing)) == 6
assert all(get_positive(test_passing)) == [2, 3, 4, 5])

# Test the function with a tuple
test_tuple = ([1, 2], [3, 4, 5])
assert len(get_positive(test_tuple)) == 2
assert all(get_positive(test_tuple)) == [2, 3])

# Test the function with a list containing a single negative number
test_single_negative = [-1]
assert len(get_positive(test_single_negative)) == 1
assert get_positive(test_single_negative) == [-1]

# Test the function with an empty list
test_empty = []
assert len(get_positive(test_empty)) == 0
``` 
This Python code defines a function `get_positive` that takes a list as input and returns a new list containing only positive numbers from the input list. It also provides various tests to validate the correctness of the function, including testing with different input scenarios (lists with positive and negative numbers, a tuple, a single negative number, and an empty list).