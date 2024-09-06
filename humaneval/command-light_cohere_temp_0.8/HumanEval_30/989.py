```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([0])
assert not get_positive([9, -9])

```
This function, `get_positive`, takes a list as input and returns a new list containing only the positive numbers from the original list. The function uses list comprehension to filter out the positive numbers from the input list.