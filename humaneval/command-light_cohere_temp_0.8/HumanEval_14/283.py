```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    """
This function creates a list of all prefixes from shortest to longest, using list comprehension and the `join` method. The test suite consists of passing the string 'abc' to the function and checking the returned list. This results in ['a', 'ab', 'abc']. 
```