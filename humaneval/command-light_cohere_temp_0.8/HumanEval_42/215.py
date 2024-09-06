```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

#Test case 1
assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

#Test case 2
assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 4, 10, 1, 124])

#Test case 3
assertEqual(incr_list([]) [], [0])
```
The `assertEqual` function is used to check the expected results of the `incr_list` function against the actual results of each test case.

This code follows the DRY principle and can easily be adapted for other similar problems.