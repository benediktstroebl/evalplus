Here's a self-contained Python function that filters an input list of strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings and returns list with matching substrings.

    # List comprehension to filter strings with the given substring
    return [str for str in strings if substring in str]
```

This function utilizes a List comprehension to iterate through each string in the input list. The if the substring is found in a string, it is added to the new list. 

This function is self-contained, and it efficiently filters the input list for the specified substring.