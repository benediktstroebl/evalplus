```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string() if prefix != '' and any_prefixes(prefix) not []]

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('123') == ['123']
    assert all_prefixes('x Caribou') == ['c']

test_all_prefixes()
```
This script defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest in the input string. It uses list comprehension and any with an additional condition to filter out prefixes that are empty and also any prefixes of the same length. The test cases cover a following:
1. Test with a empty input string
2. Test with input strings that only contain numbers (from 1 to 3 characters). 
3. Test with a input string that only contains one character.