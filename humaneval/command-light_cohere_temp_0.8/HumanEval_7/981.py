```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain given substring."""
    return [s for s in strings if s.find(substring)]

 ```.pass_tests_ python code with a function to filter strings that contain a given substring. 

The function uses the Python's list comprehension to filter the strings based on whether the substring is found in each string.