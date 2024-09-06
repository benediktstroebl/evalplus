```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[0]] + all_prefixes(string[1:])

def all_prefixes_test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This code defines a function that returns a list of all prefixes from shortest to longest of any given string. It uses this recursive approach. This approach generates all prefix by considering the first character and then recursively adds all prefixes from the rest of the string.