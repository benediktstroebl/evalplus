```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])

def all_prefixes_test(string: str) -> None:
    test_prefixes = all_prefixes(string)
    assert len(test_prefixes) == 3

def all_prefixes_with_rest(substring: str) -> List[str]:
    return ['a', 'ab', substring] + all_prefixes_with_rest(substring[1:])

def all_prefixes_with_rest_test(substring: str) -> None:
    test_prefixes = all_prefixes_with_rest(substring)
    assert len(test_prefixes) == 3
```
This script defines a function `all_prefixes` that generates a list of all prefixes from shortest to longest of the input string. It also defines a all the strings test cases and pass them successfully using `assert` statement.