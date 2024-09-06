```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('31') == [' ThirtyOne', '30', '31']
    assert all_prefixes('abc#def') == ['#def', 'abc', 'abcf']
    assert all_prefixes('') == []
test_all_prefixes()
``` 
This script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest. It uses list comprehension to filter out any characters that are not a part of the string.