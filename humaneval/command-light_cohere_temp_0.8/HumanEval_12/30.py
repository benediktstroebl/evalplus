Here is a self-contained Python script that includes the function `longest()`, which returns the longest string from a list of strings:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings:
        return None

    max_length = 0
    longest_string = ""

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string

    return longest_string

#Test case 1:
>>> longest(['a', 'b', 'c'])
'a'

#Test case 2:
>>> longest(['a', 'bb', 'ccc'])
'ccc'

#Test case 3:
>>> longest([])
None
```

In the above code, we have a function `longest()` that accepts a list of strings as an argument. The function initializes variables to keep track of the longest string and its length. It then loops through each string in the list and compares its length with the current maximum length. The string with the longest length is then stored in the `longest_string` variable. Finally, the function returns the longest string as its output.