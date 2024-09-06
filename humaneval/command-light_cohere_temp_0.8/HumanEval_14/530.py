```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string"""
    return [''.join(). prefix for prefix in reversed_prefixes(string) if prefix]

def reversed_prefixes(string: str) -> List[str]:
    return [prefix[::-1] for prefix in all_prefixes(string)]

def all_prefixes_test() -> None:
    """ Test function to check the correctness of all_prefixes"""
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

def reversed_prefixes_test() -> None:
    """ Test function to check the correctness of reversed_prefixes"""
    assert reversed_prefixes('abc') == ['bc', 'ab', 'ac']

# Run all tests when the script is executed
all_prefixes_test()
reversed_prefixes_test()
```

The script defines two functions: `all_prefixes` and `reversed_prefixes`. The first function generates all prefixes from the shortest to the longest using the `prefix` method. The second function utilizes list comprehension to achieve this. The second function creates a reversed version of the `prefixes` using slicing.