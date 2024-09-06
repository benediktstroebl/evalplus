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

This script defines a function called `longest` that takes a list of strings as input and returns either the longest string in the list or `None` if the list is empty. The function first checks if the list is empty, and if so, returns `None`. If the list is not empty, the function then uses the `max` function with a custom key function to find the longest string in the list. The function then checks if the longest string is the longest string in the list by checking the length of that string against the maximum length of all strings in the list. If it is indeed the longest string, it returns that string, otherwise, it calls itself again with the list of strings excluding the longest string, until it finds the single longest string and returns it. 

This approach ensures that the function handles multiple strings of the same length by returning the first one in the list, and it gracefully handles an empty list by returning `None`.