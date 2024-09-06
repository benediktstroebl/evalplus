```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '']
```
These two lines create a function all_prefixes that takes a string as input and returns a list of all prefixes. The List[str. 

Then, a conditional check is used to iterate over each character in the input string. The check returns True if the string, otherwise, it returns False, effectively skipping the character.