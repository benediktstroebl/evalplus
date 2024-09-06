```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join[:string.find(char)] for char in string]

# Test cases
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
```
This code defines a function all_prefixes that returns a list of all prefixes of a given string. It uses a string.find() method to find a first character of each prefix, then slice the rest of the string with the start index. The function is tested with the test_all_prefixes function, which checks if the function returns the correct output for the given string 'abc'.