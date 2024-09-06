Here is a self-contained Python script that solves the problem of finding all prefixes in a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string
    """
    return [w for w in string if w != '']
```

This script provides a function that generates a list of prefixes from the shortest to the longest characters in the input string. You can use this best function to solve the problem in a markdown code block, as shown below:
```python
# Problem: Find all prefixes in a string
# Solution: Python script with a self-contained function
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string
    """
    return [w for w in string if w != '']
```