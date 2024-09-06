```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len)
# Example usage
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: c
```
This script defines a function called longest that takes a list of strings as input. It uses the max function with the key argument set to len to find the maximum length among the strings.