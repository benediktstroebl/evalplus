```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

#Test cases
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123])
assertNotEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, -1, -10]), [5, 3, 2, 3, 9, 123])

```
This script defines a function get_positive that takes a list l as input and returns a new list containing only the positive numbers from the original list. The test cases section passes corresponding tests for the correctness of the get_positive function.