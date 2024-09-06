```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return [''.join(). smallest prefix is an empty string, so we start by pushing any character
    """
    prefixes = [c for c in string if c != '' and not isprefix(string, c)]
    return prefixes 

def isprefix(string, prefix):
    """ Check if a prefix is a valid prefix of the input string """
    return prefix.isdigit(prefix[0]) and all(c.isdigit() for c in string for c in prefix[1:])

test_all_prefixes() : List[str]
def test_all_prefixes(string: str) -> None:
    """ Test the all_prefixes function with various inputs """
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('aaa') == ['a']
    assert all_prefixes('123') == ['1', '23']
    assert all_prefixes('abc123') == ['abc']
    assert all_prefixes('34') == ['34']
    assert all_prefixes('aa') == []
    assert all_prefixes(' foo123 ') == ['foo123']
    assert all_prefixes('') == []
    assert all_prefixes('abcde') == ['abcde'] 
    assert all_prefixes('abc def ghi') == ['abc', 'abcdef', 'def', 'ghi'] 

if __name__ == "__main__":
    test_all_prefixes('abc') 
``` 
This script defines a function that returns a list of all prefixes in the string from shortest to longest, and provides a function to test this function with various inputs.