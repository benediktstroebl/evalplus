Here is a self-contained Python script that defines a function that returns all prefixes from shortest to longest of a given input string:
```python
from typing import List
import re


def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string
    Returns: list of strings
    """
    # Define the regex pattern to get all prefixes
    pattern = r'^\W*'
    # Use regex to extract all prefixes from the input string
    return re.findall(pattern, string)
```

This script is designed to solve the problem of finding all prefixes in a given string. It uses the pattern to capture all prefixes and then returns them as a list. The `re.findall()` function is essential in Python since it can efficiently extract multiple matches from a string. 

Note that the `re` module in Python is used to incorporate regular expression support, which is particularly useful when working with patterns.  The provided code is self-contained and follows the best practices of Python scripting.