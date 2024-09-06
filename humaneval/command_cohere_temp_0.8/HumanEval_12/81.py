Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(longest_string) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longest_string]
    )
```

This script defines a function called `longest` that takes in a list of strings and returns either the longest string in the list or `None` if the list is empty. The function first finds the longest string using the `max` function and the `key` parameter to specify that the length of each string is the criterion to consider for grouping them into a candidate value to be maximized. In case there is more than one string of the same length, the function removes all of them apart from the first one and recursively calls itself on the rest of the strings, considering only strings different from the longest string found in the previous iteration. 

Here's an example of how you can use the provided code:
```python
>>> longest(['a', 'bb', 'ccc'])
'ccc'
>>> longest(['abc', 'ab', 'abcd'])
'abcd'
>>> longest(['a', 'b', 'c', 'a'])
'a'
>>> longest([])
None
``` 

The examples above showcase test cases for the function, where it is demonstrated that the function returns the longest string in the list while being resilient to lists with different forms of the longest string or being empty. 

This solution should be self-contained and easy to understand, and it should solve the problem for which you provided a markdown code block.