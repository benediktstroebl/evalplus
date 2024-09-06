```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char.isalpha()]

def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("Hello, world!") == ['H', 'llo', 'h', ' Worlds']
    assert all_prefixes("Codecademy") == ['c', 'co', 'code', 'cad']

test_all_prefixes()
```  This script defines a function `all_prefixes`, which takes a string `string` as input and returns a list of all prefixes from shortest to longest of the input string.  using the  `char.isalpha()` to filter out all list of prefixes.  The filter is applied to each character in the string using list comprehension and the `isalpha()` method.  This filter returns a string `string` to check if the character is an uppercase letter.