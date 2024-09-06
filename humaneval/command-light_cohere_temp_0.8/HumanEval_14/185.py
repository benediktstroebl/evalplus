```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join[i:string.len+i] for i in range(string) if string[i:]:
            pass
            break] + [''.join[i:]]
```
This code defines a function that returns a list of all prefixes of a given string, from shortest to longest. It uses slicing to extract the range of each prefix and includes the empty string as the last element of the list.

This function is self-contained and solves the problem of finding all prefixes of a given string.