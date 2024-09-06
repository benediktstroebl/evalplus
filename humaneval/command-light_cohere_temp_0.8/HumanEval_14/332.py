```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(string[i]) for i in range(len(string)) if string[i] != '']

# Tests
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```  This script defines a function that returns a list of all prefixes from the shortest to the longest characters in the input string. It uses list comprehension to iterate through the characters of the string and checks if each character is the empty string, if so, it is added to the list of prefixes.