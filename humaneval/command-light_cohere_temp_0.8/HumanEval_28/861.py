```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join(x+'\n' for x in strings)

#Test case 1: empty list
assert concatenate([]) == ''

#Test case 2: single string
assert concatenate('a') == 'a'

#Test case 3: two strings
assert concatenate(['a', 'b']) == 'ab'

#Test case 4: three strings
assert concatenate(['a', 'b', 'c']) == 'abc'
```
This script defines a function called `concat` that takes a list of strings as an argument and returns the concatenated string. It then passes four test cases to verify its correctness.