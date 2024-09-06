Here is a Python script that contains a self-contained function that solves the problem of finding all prefixes in a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(x) for x in string. string(string) if x not in "abcdefghijklmnopqr"]
```
This code defines a function `all_prefixes` that takes a string as input and uses a generator expression to create a list of prefixes from the input string. It removes common characters and keeps only the characters as potential prefixes. 

This is a self-contained and concise solution to the problem of finding all prefixes in a given string.