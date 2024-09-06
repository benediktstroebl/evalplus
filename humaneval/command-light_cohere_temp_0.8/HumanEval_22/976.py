```python
from typing import List

def filter_integers(values:
    """
    filtered_ints = [x for x in values if isinstance(x, int)]
    return filtered_ints

filtered_integers = filter_integers(['a', 3.14, 5])
print(filtered_integers)  # Output [5]

filtered_integers = filter_integers([1, 2, 3, 'abc', {}, []])
print(filtered_integers)  # Output [1, 2, 3]

try:
    filtered_ints = filter_integers([1, 2, 3, 'abc'])
except TypeError:
    print("Error occurred")

try:
    filtered_ints = filter_integers([1, 2, 3])
except TypeError:
    print("Error occurred")
```
The function filter_integers takes a list of values as input and returns a list of integers.

The function first iterates over the input list and converts each element to an integer using the isinstance function. The converted integers are then added to a new list called filtered_ints.

Finally, the function returns the filtered_ints list, which contains only the integers from the original input list.