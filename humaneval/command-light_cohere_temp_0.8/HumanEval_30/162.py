```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
assertEqual(get_positive([1, 2, 3, -4, -5]), [1, 2, 3])
assertEqual(get_positive([1, -1, 2, -3]), [1, 2, 3])

```

The function `get_positive` takes a list as an argument and returns a new list with all the positive numbers from the original list. It uses list comprehension to create a new list by filtering out the positive numbers from the input list.