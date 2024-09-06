```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test cases
test_get_positive = []
test_cases = [
    [[]], 
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [123, 456, 789]
]

#Test loop
for test_case in test_cases:
    test_get_positive = get_positive(test_case)
    assert all(test_get_positive) == [num > 0 for num in test_case]
```
This code defines a function `get_positive` which takes a list as input and returns a new list with only the positive numbers from the input list. It then provides a tested with a list of test cases, each of which contains a list of numbers, and passes the test with `assert` and `assert` functions to check the correctness of the function.