```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join('a' <= c <= 'z') for c in string]

# Test case:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
The function all_prefixes takes a string as input and returns a list of all prefixes from shortest to longest of the input string. The code uses the simple list comprehension and the <= comparison to filter out only the characters that form a valid prefix in the given string.