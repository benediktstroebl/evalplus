```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    current_prefix = ""
    for char in string:
        current_prefix += char
        prefixes.append(current_prefix)
    return prefixes
```

The code uses a loop to iterate through each character in the string. At each iteration, it adds the current character to the current prefix and then adds the current prefix to the list of prefixes. Once the loop completes, the list of prefixes will contain all possible prefixes from shortest to longest.

Here is a test case to test the functionallity of the code:
```python
def test_all_prefixes():
    assert all_prefixes("abc") == ["a", "ab", "abc"]
    assert all_prefixes("abcde") == ["", "a", "ab", "abc", "abcd", "abcde"]
    assert all_prefixes("123") == ["1", "12", "123"]
    assert all_prefixes("abc123") == ["a", "ab", "abc", "abc1", "abc12", "abc123"]
``` 
The test case covers multiple scenarios to ensure the function performs as expected.