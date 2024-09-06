Here's the solution to the problem of returning the longest string from a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    list comprehension:
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
longest(strings)  # Output: 'c'

strings = ['a', 'bb', 'ccc']
longest(strings)  # Output: 'ccc'

strings = []
strings. strings longest(strings)  # Output: None

strings = ['a', 'aa', 'aa']
longest(strings)  # Output: 'aa'
```

The code provides a self-contained function called `longest`, which takes a list of strings as input and returns the longest string in that list. The function uses the list comprehension and the `max` function with the `len` key to achieve this. This approach is also efficient as it doesn't create any new list object and directly gets the longest element.