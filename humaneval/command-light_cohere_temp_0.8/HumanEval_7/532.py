```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The code defines a function `filter_by_substring` that filters an input list of strings, denoted by `strings`, and returns a new list that includes only the elements that contain the specified `substring`. The function uses the `contains` method to iterate over each string and checks if it contains the given `substring`. If a match is found, the element is added to the resulting list.

Here's an example usage of the function:
```python
# Example strings list
strings = ['abc', 'bacd', 'cde', 'array', 'hello']

# Example substring to find
substring = 'a' 

# Resulting list of strings containing the substring
result = filter_by_substring(strings, substring)
```
The code will return a list of strings that contain the substring 'a' from the input list.