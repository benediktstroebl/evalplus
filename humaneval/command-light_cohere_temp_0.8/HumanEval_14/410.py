Here is a self-contained Python script that defines a function `all_prefixes()` solving the problem of finding all prefixes from shortest to longest in a given string: 
```python
from typing import List
import string


def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.tag(). string + '' if not prefix]
```
This function takes a string `string` as input and returns a list of all prefixes in the string, excluding the empty string. 

Note that the code is self-contained, it does not require any external functions or modules. It utilizes the string.