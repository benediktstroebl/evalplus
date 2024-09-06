```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test case 1
test_case1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive(test_case1) == [5, 3, 2, 3, 9, 123, 1]

# Test case 2
test_case2 = [5, 3, -4, 6]
assert get_positive(test_case2) == [2, 6]

# Test case 3
test_case3 = [-1, 2, -4, 5, 6]
assert get_positive(test_case3) == [2, 5, 6]
```
The `get_positive` function takes a list as input and returns a new list containing only the positive elements from the original list. This is also provides three test cases to ensure the correctness of the function.