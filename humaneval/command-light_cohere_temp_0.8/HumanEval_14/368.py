```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])

def all_prefixes_test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcde') == ['abcde']
    assert all_prefixes('xx') == []
    assert all_prefixes('xyz123') == ['xyz123']

def all_prefixes_longest_test():
    input = 'azABCDEFGHIJKLMNOPQRSTUVWS'
    expected = ['a', 'AZ', 'az', 'AZ', 'aZ', 'AZabc', 'azabc']
    assert all_prefixes(input) == expected
```

This Python script defines a function `all_prefixes` that returns a list of all prefixes of a given string. The function uses back the value of `string` and slices it to access the prefixes. The first character uses the also calls the `all_prefixes` recursive function to generate the list of all prefixes using the `string` as the input.