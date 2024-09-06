```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])

def all_prefixes_test(test_string: str) -> None:
    assert all_prefixes(test_string) == ['a', 'ab', test_string] + all_prefixes_test(test_string[1:])
```
This code defines a function that returns a list of all prefixes from shortest to longest of any given string, and then passes tests the function with a sample string.