```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([5, 3, -5, -4, -1, 2]) == [ ]
assert not get_positive([]) == []
```
The `get_positive` function returns a list containing only the positive numbers from the input list. 
The test cases verify the expected results for different inputs.