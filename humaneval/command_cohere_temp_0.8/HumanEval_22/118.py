```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [val for val in values if isinstance(val, int)]
    return integers
```

The function employs a list comprehension that iterates through each value in the input list values. It checks if each value is an instance of the int class, and if so, it includes the value in the integers list. Ultimately, the function returns the resulting list of integers, which includes only the integer values from the input list. 

To ensure functionality, test the script with the following input values:
```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
```

The expected output for these input values is:
```
[5]
[1, 2, 3]
``` 
This will confirm that the function correctly filters out non-integer values from the list.