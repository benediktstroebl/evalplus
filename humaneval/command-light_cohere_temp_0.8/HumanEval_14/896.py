Here is a self-contained Python script that defines a function all_prefixes that finds all prefixes from shortest to longest of a given string:
```python
import string
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [prefix for prefix in string.add(prefix) for i,char in enumerate(string)][::-1:]

# Test cases
string_a = "abc"
string_b = "hello"
string_c = "world"
print(all_prefixes(string_a))  # ['a', 'ab', 'abc']
print(all_prefixes(string_b))  # []
print(all_prefixes(string_c))  # ['w', 'orld']
``` 
This script includes all the necessary components - the function all_prefixes, and test cases to verify its correctness.