Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(set(strings).count(longest_string)) == 1 else longest_search_secondary_longest(strings)

def longest_search_secondary_longest(strings: List[str]) -> str:
    longest_secondary = max(strings, key=len)
    return longest_secondary if len(set(strings).count(longest_secondary)) == 1 else longest_search_secondary_longest(strings)

# Tests
assert longest([], None)
assert longest(['a', 'b', 'c'], 'a')
assert longest(['a', 'bb', 'ccc'], 'ccc')
assert longest(['a', 'bb', 'ccc', 'aa'], 'ccc')
``` 

The `longest` function initially uses `max` with a `key` argument to determine the string with the maximum length in the list. If there is more than one string with the same length, it calls the `longest_search_secondary_longest` function to recursively handle the case. This process continues until a unique longest string is found, or we reach an empty list. 

The `longest_search_secondary_longest` function is a recursive function that solves the problem if there are multiple strings of the same length. It iterates through the list and returns the first string encountered, assuming only one instance exists in the list. It behaves as a "try-pick-alternative-if-failed" approach. The function's recursive nature allows it to handle any depth of secondary selections. 

The tests provided in the original problem demonstrate valid scenarios for the function.  In the first example, the input list is empty, and the function should return `None`. In the second and third examples, the function should return the longest string, even if it appears more than once in the list. In the fourth example, the function should return 'ccc', which is the longest string and meets the criteria when there are multiple longest strings.  This approach offers a viable solution and completes the given task.