Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.srt if prefix else '']:
    return [''] + all_prefixes(string[1:])

def all_prefixes_test_case(string: str) -> None:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This script defines a function that uses a generator expression to create all prefixes of a given input string, excluding the empty string. It then concatenates an empty string with the list of prefixes to get the full list of prefixes. This approach ensures efficient memory usage and does not create any redundant prefixes.