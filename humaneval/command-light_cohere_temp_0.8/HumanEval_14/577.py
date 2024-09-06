```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join([char for char in s if s != "" and char <= 'z'][0]) for s in string. 'b']
 strings are all prefixes that are lowercase and non-empty in the given input string.