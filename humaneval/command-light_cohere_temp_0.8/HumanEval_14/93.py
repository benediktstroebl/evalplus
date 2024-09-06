```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s+ '']
``` 
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```  This Python code defines a function all_prefixes that returns a list of all prefixes in a given string. It uses list comprehension to iterate over each character in the string and appends them to a new empty string, which effectively creates a prefix. The test_all_prefixes function verifies that the all_prefixes function correctly identifies and returns the correct set of prefixes for the string 'abc'.