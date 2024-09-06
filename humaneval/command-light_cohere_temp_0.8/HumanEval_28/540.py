```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""

    # Use List comprehension to join the strings
    return ''.join(s for s in strings)

# Unit tests
strings = ["", "hello", "world"]
assert concatenate(strings) == "hello world"

strings = []
strings = ["a", "bc", "cd"]
assert concatenate(strings) == "abccd"

strings = ["abc", "def", "in"]
assert concatenate(strings) == "abcdefin"

```  This script defines a function `concatenate` that takes a list of strings as input and returns a new string by concatenating the strings from the list. It also includes unit tests to verify the correctness of the function.