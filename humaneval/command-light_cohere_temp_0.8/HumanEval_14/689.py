```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != '']
``` 
This code defines a Python function that returns a list of prefixes of a given input string. The function uses a raw string characters as they `non-`, and creates a list of these characters. 
The `non-` characters are then transformed into their respective prefixes.