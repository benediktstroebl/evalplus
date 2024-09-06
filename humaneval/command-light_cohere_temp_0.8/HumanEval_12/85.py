```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string.

    Parameters:
    strings (list of str): list of strings.

    Returns the longest string in the list, or None.
    """
    print(longest("Hello"))  # Output: 13
    print(longest(["abc", "a", "bb"]))  # Output: 3
    print(longest(["aa", "bb", "a", "a", "ccc"]))  # Output: 5
    print(longest([]))  # Output: None
    ```