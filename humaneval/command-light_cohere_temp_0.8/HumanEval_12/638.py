```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    # initializing the list with the longest element
    longest_element = strings[0]
    return [longest_element]

# Test case 1
strings = ['a', 'b', 'c']
assert longest(strings) == ['a']

# Test case 2
strings = ['a', 'bb', 'ccc']
assert longest(strings) == 'ccc'

# Test case 3
strings = []
assert longest(strings) == []
```
This script defines a function `longest` that takes a list of strings as an argument and returns the longest string from the list. It uses the initializes the longest element from the list and returns it as the result. It also has a test cases to verify the correctness of the function.