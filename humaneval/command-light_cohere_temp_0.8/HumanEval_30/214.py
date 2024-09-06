```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test the function with a list of numbers
test_positive = get_positive([-1, 2, -4, 5, 6])
assert test_positive == [2, 5, 6]

# Test the function with a mix of numbers and strings
test_mixed = get_positive([5, 3, -5, 2, -3, 'three'])
assert test_mixed == ['three', 2, 5, 3]

# Test the function with a list of booleans
test_booleans = get_positive([True, False, True])
assert test_booleans == [True, False]
```
The script defines a function `get_positive` that returns a new list containing only positive numbers from the input list. It also includes several test cases to ensure the correctness of the function. The tests cover a list of numbers, a mix of numbers and strings, and a list of booleans.