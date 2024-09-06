```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings
    Returns: 
    string
    """
    return ''.join(strings)
```
Here, the function concatenate takes a list of strings as an argument and uses the join() method to concatenate them into a single string. The test cases are enclosed in the >>> operator to ensure the code is executed correctly.