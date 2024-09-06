```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[0]] + all_prefixes(string[1:])

def all_prefixes_test(string: str) -> None:
    assert all_prefixes(string) == ['a', 'ab', string[0]] + all_prefixes(string[1:]),
    pass
```
This Python code defines two functions: all_prefixes and all_prefixes. The all_prefixes function returns a list of all prefixes from shortest to longest of an input string. The all_prefixes_test function tests whether the all_prefixes function correctly returns the expected output for a given input string.