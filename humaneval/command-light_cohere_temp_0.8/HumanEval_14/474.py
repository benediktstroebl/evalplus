Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of a given input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(w) for w in string if w != '']
```
This function iterates over each character in the input string and creates a new prefix by prepending the character to the empty string.