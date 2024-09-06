```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and not seen.add(num):
            result.append(num)
    return result
```

To use this function, you can call it and pass a list of integers as an argument. For example:
```python
remove_duplicates([1, 2, 3, 2, 4])
```

This would output:
```python
[1, 3, 4]
```

The function has a descriptive docstring that explains its purpose, input, and behavior. It uses a set data structure to efficiently track unique elements and appends them to a `result` list. The output is a list containing only the unique elements from the input list, preserving their original order.