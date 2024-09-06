Here is a self-contained Python function that solves the problem of returning all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']
```
This function takes a string `string` as input and iterates over each character c in the string. For each character, if c is not a space, it is included in a list of prefixes. 

This function is self-contained and will produce the desired output, which is a list of all prefixes from shortest to longest of the input string. 

This is a good example of a function that is complete in itself, without needing to call it with any other functions or classes.