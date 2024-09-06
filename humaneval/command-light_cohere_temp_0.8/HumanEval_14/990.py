```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join()[::-1] for i, h in enumerate(string) if h.endswith('.')]
```  This function uses the type hint of the string parameter to ensure that the input is a string, and then uses the slicing technique with [::-1] to reverse each character in the string and converts it into a list. The function then returns all resulting prefixes.