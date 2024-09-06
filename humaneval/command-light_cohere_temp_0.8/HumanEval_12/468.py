```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of empty list or input. """

   
    to be done.
    return max(strings, key=len)

#Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'a'

strings = ['abc'] * 5
print(longest(strings))  # Output: 'abc'

strings = []
print(longest(strings))  # Output: None

strings = ['a', 'bb', 'ccc']
print(longest("""[a,b,c,]d"""))  # Output: 'ccc'

strings = ['aa', 'bb', 'ccc']
print(longest(strings, key=len))  # Output: 'bb'

```