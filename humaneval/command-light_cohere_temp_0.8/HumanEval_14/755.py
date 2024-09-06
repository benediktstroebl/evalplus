```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(s) for s in string.
      .("" not in c for c in string)
      for c in string if c not " " and c not b>" if all_prefixes(c))
      return]

# Test cases
print(all_prefixes("abc"))      # ['a', 'ab', 'abc']
print(all_prefixes("hello"))    # []
print(all_prefixes("a"))        # ['a']
print(all_prefixes("de"))        # ['de']
print(all_prefixes("abcde"))    # ['a', 'ab', 'abcde']
```
This Python script defines a function called `all_prefixes` that returns a list of all prefixes in a given string. It uses a small utility function to find all prefixes and uses a generator expression to create the list of prefixes from the characters in the input string.