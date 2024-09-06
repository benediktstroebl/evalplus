Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(strings[1:])
```

This script defines a function called `longest` that takes a list of strings as input and returns either the longest string in the list or None if the list is empty. The function first checks if the list is empty and returns None if it is. If the list is not empty, the function then uses the `max` function with a custom key function to find the longest string in the list. The `max` function takes a list of strings and a key function that specifies how to compare the strings as input, and returns the longest string according to the given comparison. In this case, the key function is a lambda function that returns the length of the string. 

If there are multiple strings of the same length, the function returns the first one. Finally, the function returns the longest string, or if there are multiple of the same length, it recursively calls itself to process the list of strings excluding the current longest string, which is the behaviour described in the problem statement.

This script can be tested against the examples provided in the problem statement.