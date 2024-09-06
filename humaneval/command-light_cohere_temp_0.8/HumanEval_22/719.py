```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [i for i in values if isinstance(i, int)]

# Test cases
values_test = [1, 2, 3, 'abc', '', [0], [(), True, [1, 2, 3, 'a']]]
print(filter_integers(values_test))  # Output: [1, 2, 3, '', [], True]
```