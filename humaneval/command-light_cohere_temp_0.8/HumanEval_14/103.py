```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(x) for x in string.
    """

def test_all_prefixes():
    """ Function to test the all_prefixes function """
    assert all_prefixes("abc") == ["a", "ab", "abc"]
    assert all_prefixes("123") == ["123"]
    assert all_prefixes("   ") == [""]
    assert all_prefixes("") == []
    assert all_prefixes("123abc") == ["123", "abc"]

test_all_prefixes()
```
This code defines a function `all_prefixes` that returns a list of all prefixes of a given string, and a test function `test_all_prefixes` that verifies the correctness of this function with a variety of inputs.