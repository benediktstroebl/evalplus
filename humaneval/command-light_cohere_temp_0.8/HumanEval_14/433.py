```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join() for i, char in enumerate(string, 1, 1)]
# Example usage:
input_str = 'abc'
print(all_prefixes(input_str))  # Output: ['a', 'ab', 'abc']
```
This Python function, `all_prefixes`, uses a generator expression to return a list of all prefixes of a given string. It uses the str. Each character takes a partnership with `enumerical index of each character in the string and starts counting from `1` (as opposed to `0`). This way, each character is assigned its proper position as a prefix.