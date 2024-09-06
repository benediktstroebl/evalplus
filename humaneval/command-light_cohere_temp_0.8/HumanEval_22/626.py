```python
from typing import List
def filter_integers(values: 
    return [x for x in values if isinstance(x, int)]
):
    pass

# Example usage:
values = [1, 2, 3, 'abc', {}, [0]]
print(filter_integers(values))  # [1, 2, 3]

values = [1, 2, 3, 'five', [0, 1]]
print(filter_integers(values))  # ['one', 'two', 'three']

values = ['a', 3.14, 5]
print(filter_integers(values))  # [5]

values = [1, 2, 3, 'abc', {}, [0, 1, 2]]
print(filter_integers(values))  # [1, 2, 3]
``` 
The function `filter_integers` takes a list of values and returns a new list with only the integers from the input list. 
The example usage demonstrates the passing the function several test cases and printing the resulting filtered list.