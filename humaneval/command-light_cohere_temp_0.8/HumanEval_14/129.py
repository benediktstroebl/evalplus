Here's a self-contained Python function that returns all prefixes from shortest to longest of a given string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["", string, string + string[1:], string + string[:1]]
```
This function takes a string as input and returns a list of all prefixes from shortest to longest. The function uses different types and returns a list of strings as output.