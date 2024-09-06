```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_values = [item for item in values if isinstance(item, int)]
    return int_values
```

The function uses a list comprehension that iterates over each value in the input list values. It checks if each item is an instance of int using the isinstance() function. If it is, it includes the item in the int_values list. Finally, the function returns the int_values list, which will contain only the integer values from the input list. 

To run the code simply run:
```python
filter_integers(['a', 3.14, 5])
```

And similarly for the second example:
```python
filter_integers([1, 2, 3, 'abc', {}, []])
``` 
This will yield the expected output of `[5]` and `[1, 2, 3]` respectively, as illustrated in the docstring.