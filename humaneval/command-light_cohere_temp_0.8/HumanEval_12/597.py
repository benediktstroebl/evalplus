```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one. """

    1. Filter out empty strings 2
   's
    1. Get list of strings
   
    2. Sort the strings alphabetically
   
    3. Return the first string
   
    4. Use max input
    option
    for testing
    """
    # 1. Example empty list
   
    empty list
    >>> longest([]) is None
    # 2. Example list of strings of equal length
    >>> longest(['a', 'b', 'c']) == 'a'
    # 3. Sorting
    example
    list of strings of the same length
    >>> longest(['a', 'bb', 'ccc']) == 'ccc'
    # 4. Use optional[List for input
    This allows the function to handle empty lists gracefully
    return None if strings is empty, else strings[0]

```
Do you need any help with other coding problems?