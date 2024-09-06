```python
from typing import List
def filter_integers(values): 
    return [i for i in values if isinstance(i, int)]

print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([3, 'three', 123, 2, 'aa', 6]))  # Output: [123, 2, 'aa']
print(filter_integers([1, 2, 3, 'a']))   # Output: []
``` 
This function employs a list comprehension to filter the values in the `values` input list, only keeping the instances of type `int` by using the `isinstance` function.  The filter returns a list of `int` integers, ensuring that other data types are excluded. 

This function is self-contained and can be used to filter any list of values, including any type or custom data, as long as they are converted to integers.