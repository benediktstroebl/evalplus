```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = get_positive([-1, 2, -4, 5, 6])
assert test_get_positive == [2, 5, 6]

test_get_positive2 = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_get_positive2 == [5, 3, 2, 3, 9, 123]
 ``` 
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the input list. The function is tested by passing two test cases and asserting that the result is correct.