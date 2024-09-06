```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [string[i:]+ for i, c in enumerate(string) if c == "" and string.read() != ""]
```

def test_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
```
This code defines a function called all_prefixes that returns a list of all prefixes from shortest to longest of the input string. It uses the also a index of the string, starting from the beginning, and appends it with spaces until it reaches the end of the string. Additionally, it checks if the string has ended and if the character is blank, which means that it added a full prefix.

The test_prefixes function tests the correctness of the all_prefixes function by asserting that it returns the expected result for the input string 'abc'.