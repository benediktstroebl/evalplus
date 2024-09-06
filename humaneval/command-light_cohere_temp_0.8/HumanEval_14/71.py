```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [part for part in string.comp(string) if part else "" != ""

# Test cases
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']

test_all_prefixes()
```

The function all_prefixes takes a string as input and uses the `comp()` method of the string to iterate over all prefixes. This method returns all prefixes as a list of strings.