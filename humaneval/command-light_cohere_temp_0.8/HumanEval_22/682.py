```python
from typing import List

def filter_integers(values: List[Any]):
    """
    Filter given list for only integers
    :param values: List of any python value
    :return: List of integer
    """
    return [x for x in values if isinstance(x, int)]

#Test case 1
print(filter_integers(['a', 3.14, 5]))  # [5]

#Test case 2
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

#Test case 3
print(filter_integers([10, "20", '30', 40, False]))  # [10, 20, 30, 40]
```

This script defines a function called `filter_integers` that takes a list of any python values as an argument and returns a new list with only the integer elements from the input. The function uses a list comprehension with the `isinstance` condition to filter out the non-integer elements.