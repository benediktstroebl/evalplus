```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The function takes a list of strings and a prefix as input and returns a new list containing only the strings that start with that prefix.

For example, if you pass the list ['abc', 'bcd', 'cde', 'array'], and the prefix 'a', the function will return ['abc', 'array']. 
This is a self-contained solution and does not require any additional lists or external functions.