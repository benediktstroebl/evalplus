```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings:
        return None

    longest_length = max([len(s) for s in strings])
    return strings[strings.index(longestlength)]
``` 
This function utilizes the max function to determine the maximum length among all strings in the input list. Additionally, it uses the index to get the string with the maximum length. The return the longest string in the list.