```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with a list of values
test_positive = get_positive([-1, 2, -4, 5, 6])
assert test_positive == [2, 5, 6]

# Test the function with a mixed list of negative and positive numbers
test_mixed = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_mixed == [5, 3, 2, 3, 9, 123]
```
This code defines a `get_positive` function that takes a list as input and returns a new list containing only the positive numbers from the original input list. The function uses a testing, you can use it to process various lists and validate the results. The code also provides test cases to ensure the correctness of the function.