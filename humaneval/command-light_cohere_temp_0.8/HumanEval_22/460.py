```python
from typing import List

def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
print(filter_integers([4, 2, 7, 'abc', 1, 5]))

```
This function, named `filter_integers`, takes a list of values and returns a new list containing only the integers from the input. It uses a filter/ built-in function to perform this operation.

The output of the example usage will be:
```bash
[5]
[1, 2, 3]
[7]
```