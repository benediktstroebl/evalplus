```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix not ''] + ['']  # Initialize empty list and add empty string.
    # Initialize and list with the characters of the input string.
    for i in range(1, len(string)):
        if string[i - 1] != ' ':
            all_prefixes[i] = string[i - 1].lower()  # Append current character to the list
```
Do you need assistance with anything else?