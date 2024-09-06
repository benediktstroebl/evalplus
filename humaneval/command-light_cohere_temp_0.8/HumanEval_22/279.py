```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

filter_integers(['a', 3.14, 5])  # ['5']
filter_integers([1, 2, 3, 'abc', {}, []])  # [1, 2, 3]
filter_integers([1, 2, 3, True, (])])  # [1, 2, 3]
filter_integers([1, 2, 3.y.4])  # #.int
```

``` 
This code defines a function called `filter_integers` that takes a list of values as an argument and returns a new list containing only the integers from the input list. The function uses the filtering logic and returns the resulting list of integers.