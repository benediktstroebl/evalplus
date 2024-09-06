```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return ["".join(c) for c in string if c != ' ', 'a']

# Tests
test_string = "abc"
assertEqual(test_string, all_prefixes(test_string))

# Additional tests are possible here, such as with different strings, lengths, etc.
```