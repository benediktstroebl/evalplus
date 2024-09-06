```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string) if char != ' ' and i != 0]

# Test cases
test_ prefixes = all_prefixes("abc")
should["abc"]
should["ab"]
should(["a"])
should([])
```
The script defines a function `all_prefixes` that returns a list of all prefixes of a given string. It uses the recursive approach, iterating through each character and checking if it's not a space or the end of the string, then adding it to the list of prefixes.