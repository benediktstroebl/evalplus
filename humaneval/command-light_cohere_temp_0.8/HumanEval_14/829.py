```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(['a', 'ab', string]))  # [].join(L) is not needed in Python 3.0
``` 

This function takes a string as input and returns a list of all prefixes from shortest to longest. It uses the same built-in list comprehension and creates a new list with the desired output.