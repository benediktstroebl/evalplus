```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various lists
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123])
assertEqual(get_positive([]), [])
assertEqual(get_positive([-123, 0]), [0])
assertEqual(get_positive([-1, -2, -3, 4, 5, 6, -7]), [4, 5, 6, -3])

```
This function, `get_positive`, returns a new list containing only the positive elements from the input list. It utilizes list comprehension with a conditional statement to filter out the positive values from the list.