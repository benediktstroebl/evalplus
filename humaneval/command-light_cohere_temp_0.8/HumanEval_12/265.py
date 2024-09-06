```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.

    if not strings:
        return None

    max_length = 0
    longest_str = ""
    for str in strings:
        if len(str) > max_length:
            max_length = len(str)
            longest_str = str

    return longest_str
# uncomment below to run the tests
# print(longest([['a', 'bb', 'ccc'], ['a', 'bb', 'ccc']]) )
# print(longest(['a', 'bb', 'ccc']))
```
The function `longest()` takes a list of strings as input and returns the longest string from the list. 
The function first checks if the input list is empty. It returns `None` if the empty. Then, it initializes a `max_length` and `longest_str` variable to keep track the maximum length and the current longest string. 

Finally, it iterates through the list of strings and updates the `max_length` and `longest_str` variables accordingly.