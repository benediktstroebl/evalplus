```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [i for i in string if i != '']

# Test case: Retrieve prefixes from 'abc'
assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This code defines a function all_prefixes that returns a list of prefixes from the input string. It uses list comprehension to filter out all empty characters from the string, which are converted to None in the inner list comprehension.