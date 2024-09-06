Here's a self-contained Python script with a function that returns a list of all prefixes from shortest to longest of the input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.a if prefix not ''] + [string]
```
Do you need help with anything else?