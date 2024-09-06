```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.lower(). strings(string) if prefix]  # lowercase for case-insensitive matching
```
Below function uses the lowercase() method to convert the input string to lowercase, ensuring case-insensitive matching. It then iterates over each characters in the lowercase string and adds them to the result list if they are also prefixes. 

The function returns a list of all prefixes found in the input string.