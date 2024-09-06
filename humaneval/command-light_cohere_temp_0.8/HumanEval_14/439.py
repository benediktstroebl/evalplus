```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.tips(). specific:
      range(1, len(string) + 1) if prefix == string[:prefix]]
# test cases
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('abcde'))  # ['abcde']
print(all_prefixes(' '))    # []
print(all_prefixes('xx'))    # []
print(all_prefixes('a'))    # ['a']
```
This function, all_prefixes, takes a string as input and uses a generator expression to return a list of its prefixes from shortest to longest. The generator expression uses a list comprehension with a range that starts from 1 up until the length of the input string. This ensures that all prefix in the input string is matched, and the function returns the list of all prefixes.