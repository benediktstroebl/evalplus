```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.get(str.split()) if prefix else:
    # if it's empty, it's a prefix
    return []  # empty string is a prefix

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcde') == ['abcde']
    assert all_prefixes('abcfijk') == ['a', 'bc', 'c']
    assert all_prefixes('') == []
    assert all_prefixes("-abc") == ['-abc']
    assert all_prefixes(" foo") == ['foo']

test_all_prefixes()
``` 
This Python script defines a function all_prefixes that returns a list of all prefixes in a given string. 

The function uses the str.split method to split the strings into substrings and then uses list comprehension to filter the prefixes. 

The test_all_prefixes function contains a series of assertions that verify the correctness of the function by passing different input strings and expected output through the function.