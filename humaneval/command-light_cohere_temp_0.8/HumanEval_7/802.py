Here's the solution to the markdown code block problem:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring.

    # Create a filter using the filter by checking prefix, exact match, and suffix
    filtered = [x for x in strings if x.startswith(substring) or string.endswith(substring)]

    return filtered
```
This function utilizes Python's List comprehension and the startsswith and endswith methods to filter the strings based on whether they contain the given substring as a prefix, exact match, or a suffix. It returns the filtered list containing only the strings that pass the filter.