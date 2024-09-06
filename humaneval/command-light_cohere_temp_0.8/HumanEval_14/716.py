```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(). all(...)
    for i in range(1,len(string)+1):
        if string[:i] not in all_prefixes(string):
            all_prefixes.extend(string[:i])
    return all_prefixes(string)
    ```