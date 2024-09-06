```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in range(len(string) + 1)]  # using list comprehension with a generator expression
    # actual values are the characters of the string, iterated from shortest to longest
    # this is O(n)
    # the list comprehension above ensures unique values
    # test cases:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('aa') == ['a']
    assert all_prefixes('') == []
    assert all_prefixes('x-30a') == ['x', '-30', '30a']
    assert all_prefixes('hello world 123') == ['h', 'el', 'll', 'orld', '123']
```  This script defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string. It uses a A list comprehension to generate all possible prefixes from the characters of the input string, in order of their length.