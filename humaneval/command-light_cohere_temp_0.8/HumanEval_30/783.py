```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Test case 2: []
assert get_positive([]):     assert True

# Test case 3: [[-1, 2, -4, 5, 6])
assert get_positive([-1, 2, -4, 5, 6]) == [-1, 2, 4, 5]

# Test case 4: ([5, -9])
assert get_positive([5, -9]) == [5]

# Test case 5: ([0, -1, 2, 3, 4, 5])
assert get_positive([0, -1, 2, 3, 4, 5]) == [0, -1, 2]
```
The provided Python script defines a function `get_positive` that returns a list of positive numbers from an input list. It uses list comprehension to iterate through the elements in the input list and filters out negative numbers. The script then provides several test cases to validate the correctness of the `get_positive` function.