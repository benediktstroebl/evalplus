```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping occurrences.
    :

    The substring can contain any characters, including special ones.
    Example: Returns the number of non-overlapping occurrences of the substring in the string.
    """

    function uses the provided by the "count_re" library and its efficient "findall" function to iterate over all substrings and count their occurrences. 
```

Here's the code: 
```
from collections import Counter
import re

def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping occurrences.
    :

    The substring can contain any characters, including special ones.
    Returns: number of non-overlapping occurrences of the substring in the string.
    """
    pattern = re.compile(substring)
    while match = re.findall(pattern, string)
    return len(match)
    """