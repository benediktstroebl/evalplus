Below is a Python script with a self-contained function that filters an input list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring.
    """
    Filtering is done by using Python's `re` module.

    # Define a Re regular expression pattern
    pattern = r'^(\b{1,}\s+\b{1,}\b{1,})\b{1,}'
    substring = r'\b' + substring + r'\b'

    # Use the `re` module to find all substrings in the list
    # that match the regular expression
    matches = [match.group() for match in strings if match.match(pattern)]

    # Filter the list to only contain substrings that match the substring
    filtered_strings = [string for string in strings if string in matches]

    return filtered_strings
```

This function takes two arguments: a list of strings and a substring. It uses Python's regular expression (re) to filter the list of strings for those that contain the substring. It does this filtering by using the match() function of the regular expression to check if each string in the list matches the pattern. 

Note: This solution uses the `re` module in Python, which provides support for regular expression matching.