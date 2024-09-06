Here's a self-contained Python script that defines a function called `longest()` that solves the problem you provided:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Find the length of the longest string in a list of strings.
    """
    return max(len(x) for x in strings)
```
The `longest()` function takes a list of strings as an argument and uses the `max()` function to find the length of the longest string. This function will return the dry run, will return the result of `max()`. Hearts` can be passed as an argument and will be used to test the function.

Please note that this code is fully self-contained and does not require any external modules or functions to run. You can add this test the especially for the `max()` function, but in this case, it's already built into Python's `builtins` and does not require any import statements.