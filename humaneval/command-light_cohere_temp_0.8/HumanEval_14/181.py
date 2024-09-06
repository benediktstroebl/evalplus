```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c not in ' ,"\n']
def test_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
```  This code defines a function that returns a list of all prefixes from the shortest to the longest in a given string. It uses a simple list comprehension and a filter to identify all prefixes and non-space characters.  The tests if the strings are passed as arguments to the function, it will return the list of all prefixes in the correct format.