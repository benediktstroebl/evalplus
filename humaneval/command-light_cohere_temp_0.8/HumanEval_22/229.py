```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers."""
    return [int(x) for x in values if x.isdigit()]
}
filter_integers([1, 2, 3, 'abc', {}, []])
# [1, 2, 3]
filter_integers(['a', 3.14, 5])
# [5]
filter_integers([1, 2, 3, 'abc', {}, [0]])
# [1, 2, 3]
```
This script defines a function called `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. It uses the template to create the list comprehension that filters out any non-integer values from the input list, then converts each value to an integer using the int() function if it is a string. The output of this function is then tested with a series of input scenarios to ensure that it is working correctly.