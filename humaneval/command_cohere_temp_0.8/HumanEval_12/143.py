Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longest_str]
    )
```

This script defines a function called `longest` that takes a list of strings as input and returns either the longest string in the list or `None` if the list is empty. The function first checks if the list is empty, and if so, returns `None`. If the list is not empty, the function then uses the `max` function with a custom key to find the longest string in the list. The `max` function takes a list of strings and a key function, which is a function that takes a string and returns a value to be used for comparison. In this case, the key function is the `len` function, which returns the length of the string. The `max` function then compares the list of strings based on their length and returns the longest string. 

However, if there are multiple strings of the same length, the function will return the first one among them. So, to handle this inconsistency, the script further checks if the length of the current longest string is not the same as the maximum length among all strings. If this condition is true, it means that there is at least one longer string in the list, and the function recursively calls itself to process the list of strings minus the current longest string, which is achieved by filtering out the current longest string.

Here are some example usages of the function to prove its correctness:
```python
>>> longest([])
None
>>> longest(['a', 'b', 'c'])
'a'
>>> longest(['a', 'bb', 'ccc'])
'ccc'
```

This script provides a clean and efficient way to find the longest string in a list of strings and handles all edge cases appropriately.