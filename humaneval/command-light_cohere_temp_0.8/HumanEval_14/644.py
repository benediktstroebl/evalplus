```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != '']
```
The code defines a function called **`all_prefixes`** that takes a string as input and returns a list of all prefixes in the input string, excluding the empty string itself.  This generate all list of non-empty characters, the function applies a list comprehension with a condition that checks if each character is not the empty string, effectively generating all prefixes in the input string.