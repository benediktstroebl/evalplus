Here's the code you requested:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [i for i in string if i.startswith(string[0]]
```

This function loops through each character in the string and checks if it starts with the first character of the input string. It then returns a strings that start with the specified prefix are returned.