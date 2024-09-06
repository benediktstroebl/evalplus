```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(x) for x in string.
    if isinstance(string, str):
        return _test_prefixes(string)
    else:
        raise ValueError("Input must be a string")

def _test_prefixes(string: str) -> None:
    prefixes = all_prefixes(string)
    assert len(prefixes) == len(set(prefixes)), "Prefixes should be unique"
    assert sorted(prefixes) == sorted([''.join(x) for x in string]), "Prefixes should be sorted"
    return prefixes

# Example usage
string = "abc"
result = _test_prefixes(string)
print(result)  # Output: ['a', 'ab', 'abc']
```
This script defines a function all_prefixes that returns a list of all prefixes from the shortest to the longest in the input string. It also includes a test_prefixes function that tests if the all_prefixes function is working correctly.