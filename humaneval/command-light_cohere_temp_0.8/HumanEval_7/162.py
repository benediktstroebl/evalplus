Here's the solution to the markdown code block problem:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring.
    :param strings: List of strings to filter
    :param substring: The substring to filter
    :return: List of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```
This function utilizes the contains() method to check whether each string in the input list contains the given substring, and then returns a new list containing only those strings that pass the test. The function is self-contained, efficient, and provides a clear and concise solution to the given problem.