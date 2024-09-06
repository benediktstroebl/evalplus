```python
from typing import List

def filter_integers(values:
    return [int(x) for x in values if x.isinstance(int)]

filter_integers(['a', 3.14, 5])
# [5]
filter_integers([1, 2, 3, 'abc', {}, []])
# [1, 2, 3]
``` 
This script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers from the input.  The test that function using the `isinstance` operator, which checks if a value is an instance of the built-in `int` type. 
This ensures that only integers are included in the output list.