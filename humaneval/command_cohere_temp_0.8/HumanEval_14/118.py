```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    current_prefix = ''
    for char in string:
        current_prefix += char
        prefixes.append(current_prefix)
    return prefixes
```

The function `all_prefixes()` uses a loop to iterate through each character in the input string. For each character, it appends it to the current prefix and then adds the current prefix to the list of prefixes. Initially, `current_prefix` is an empty string, and for the first character of the input string, it becomes the prefix. This way, we account for the case where the input string has a length of zero, and there is no prefix. Lastly, the list of prefixes is sorted in place from shortest to longest, as the shortest prefix is the one with no characters, followed by the single-character prefixes, and lastly, the full string itself.

Here is an example usage of the function:
```python
print(all_prefixes('abcd'))
```
The function would return the following list of prefixes: ['', 'a', 'ab', 'abc', 'abcd'].