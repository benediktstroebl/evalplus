```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix.isalpha(prefix)]
```

This function employs a generator expression and the isalpha() string method to extract all prefixes from the given string. The isalpha() method identifies all alphabetic characters, which are the prefixes in the string.