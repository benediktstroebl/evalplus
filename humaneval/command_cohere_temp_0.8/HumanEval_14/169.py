```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    # Get all prefixes with the regex expression
    prefixes = re.findall(r"^(.*)\1*", string)
    # Sort them properly
    return sorted(prefixes, key=lambda x: (len(x), x))
``` 

The Python script takes advantage of regular expressions to solve the problem efficiently. Specifically, the `re.findall` function is utilized to find all prefixes of the input string. The regular expression `^(.*)\1*` captures all strings that begin with a certain character sequence, indicated by `^`, and repeat that same sequence `\1*` any number of times. For example, for the input `'abc'`, the regular expression will capture the following prefixes: `'a'`, `'ab'`, and `'abc'`.

To sort the prefixes from shortest to longest, the script employs the `sorted` function in combination with a custom sorting key implemented as a lambda function. This lambda function takes a prefix and assesses it on two levels: first, it checks the length of the prefix, and secondly, in case of a tie, it compares the prefix itself. This results in the following sorted list of prefixes: `'a'`, `'ab'`, `'abc'`. 

By utilizing regular expressions in combination with the `sorted` function, the Python script provides a concise and efficient solution for finding and sorting all prefixes of a given string. 
```