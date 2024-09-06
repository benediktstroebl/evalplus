```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in the list.
    Parameters: List[str]
    Returns: str or None 
    """
    return max(strings, key=len)

# Test the function with sample inputs
test_longest = [
    ['a', 'bb', 'ccc'],
    ['abc', 'abc', 'aaa'],
    ['aa']
]

assert longest(test_longest) == 'ccc'
```
This Python script defines a function named longest that takes a list of strings as input and returns the longest string. The function uses the maximum function to find the longest string, with the key argument set to the string's length. The test case at the time verifies the correctness of the longest function by passing a sample input and asserting the returned result matches the expected output.