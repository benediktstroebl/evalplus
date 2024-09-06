```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix.isalpha(prefix)]
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest in a string, it uses the isalpha function to check if a prefix is an alpha and then adds it to the result. 
This function is self-contained and can be used as a standalone solution for the problem.