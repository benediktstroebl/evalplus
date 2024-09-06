```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.

    # if empty list
   
    if not strings:
        return None

    # find the length of the longest string
    max_length = max([len(string) for string in strings])

    # find the longest string
    longest_string = ''.joinstrings[strings.index(strings[max_length)]

    return longest_string
```
I hope this code provides a solution to the problem, which is to find the longest string in a list of strings. The code utilizes the method and returns the longest string found.