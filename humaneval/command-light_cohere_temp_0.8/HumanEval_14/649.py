```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix.isalpha(string)]
```

This Python code defines a function called `all_prefixes` that aims to return a list of all prefixes from the shortest to the longest occurring prefix in the input string. 

To achieve this, it uses list comprehension to iterate over each character in the string and checks if each character is the starting letter of a new prefix using the `isalpha` function. 

The resulting list contains all the prefixes found, from shortest to longest, which are returned as a list of strings.