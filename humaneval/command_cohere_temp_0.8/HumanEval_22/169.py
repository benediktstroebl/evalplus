```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The above code snippet takes a list of values of any type and returns a list of integers present in the list. It utilizes list comprehension and the `isinstance()` function to achieve this. The type annotation `List[Any]` indicates that the function takes a list that could contain any type of value, and the return type is specified as `List[int]`. 

This function would pass the test cases mentioned in the original problem, as it would successfully filter out integers from the given lists. 

It is important to note here that the function assumes that the list may contain values of various types other than integer, including non-numeric strings and non-hashable objects like dictionaries and lists. If the list is assumed to contain only numeric strings that can be converted to integers, it could be stricter to explicitly convert the elements to integers as well during filtering, as below: 
 ```python
def filter_integers(values: List[str]) -> List[int]:
    return [int(x) for x in values if x.isdigit()]
``` 

This filtered list of integers can be later converted back to strings if needed, using a lambda function: `['{}'.format(x) for x in integers]`.