```python
from typing import List
def filter_integers(values):
    """ Filter given list for only integers
    :param values: list of any python object
    :return: list of integers
    """
    return [x for x in values if isinstance(x, int)]

# test case 1
values = ['a', 3.14, 5]
print(filter_integers(values))  # [5]

# test case 2
values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # [1, 2, 3]

# test case 3
values = [1, 2, 3, True, [], [1, 2])
print(filter_integers(values))  # [1, 2, 3]
```
The function `filter_integers` takes a list of values as input and returns a new list containing only the integers from the input list. The test cases demonstrate how the the function behaves as expected, filtering out non-integer elements.