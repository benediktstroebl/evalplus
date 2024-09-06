Here's the self-contained function along with the markdown code block: 

```python
from typing import List

def filter_integers(values: List[Any]):
    """ Filter given list for integers"""
    return [x for x in values if isinstance(x, int)]

# Example usage in markdown code block
>>> filter_integers(['a', 3.14, 5])
 [5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
 [1, 2, 3]
 ``` 

This script defines a function `filter_integers` that takes a list of any python objects and returns a new list containing only the integers from the original list. 

The function uses the typing feature in Python to automatically infer the type of values in the input list and uses the `isinstance` method to filter only the integers from the list.