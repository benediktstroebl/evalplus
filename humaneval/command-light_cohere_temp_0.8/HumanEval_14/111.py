```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(). all
    if not string: return []
    if len(string) == 0: return []
    if string == '': return ['']
    return [i for i in string if i.start <= i <= len(string)]
```  This script defines a function all_prefixes that takes a string as an argument and returns a list of all prefixes from the shortest to the longest characters in the string.