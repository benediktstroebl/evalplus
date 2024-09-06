```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.lower() if prefix in string.

    :match method
    of any character, each one is a prefix
 
return ['a', 'ab', 'abc']
``` 
This Python script defines a function `all_prefixes` that accepts a string as input and returns a list of all prefixes present in the input string. 

The function uses the `match` method of each character in the string, where each one is a prefix.  This process returns a `reversed` version of each character, which ensures that all prefixes are included.