```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.

    :param values: List of any Python values.
    :return: List of integers contained in the input list.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result
```

This function takes a list of various Python values and returns a list of integers that were present in the input list. It does so by using a list comprehension that checks if each value in the input list is an instance of the int class, and if so, including it in the result list. The function includes type annotations that help make the code more readable and provide hints to the reader about what each variable should be. 

To test this function, you can call it with different lists of values and verify that the output contains only integers. 
For example:
```python
filter_integers([1, 2, 3, 'abc', 10, None])
```

Expected output:
```
[1, 2, 3, 10]
```

This demonstrates the function's ability to filter out non-integer values from the input list and return a list containing only integers.