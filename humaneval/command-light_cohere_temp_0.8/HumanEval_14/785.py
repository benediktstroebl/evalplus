```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.split() if prefix != '']

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('') == []
    assert all_prefixes('123') == ['1', '23']
    assert all_prefixes(' ') == ['']
    assert all_prefixes('   ') == ['   ', '']
test_all_prefixes()
``` 
This code defines a function called all_prefixes that returns a list of all prefixes in a given string. The function splits the the string and then returns a list of prefixes from the resulting characters. 

It has also defined a test case with a series of test statements that checks the function's correctness with different inputs. 

Note: It uses the typing module to provide type hints and better documentation for the code.