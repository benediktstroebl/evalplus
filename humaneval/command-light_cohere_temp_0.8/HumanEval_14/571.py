```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.PY longest_prefixes(string)][::-1]

def longest_prefixes(string: str) -> List[str]:
    return [string[i:]: for i in range(len(string)) if string[i:].count(string[i]) == len(string)]
```
The function returns a list of all prefixes from the shortest to the longest occurring prefixes in the input string. It utilizes a example usage below:
```python
print(all_prefixes('abc'))
# ['a', 'ab', 'abc']
```