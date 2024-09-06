```python
from typing import List
def longest(strings: List[str]): 
    """
    Returns the length of the longest string in the list.
    """
    list must be of non-empty strings
    return max(map(len, strings))

# Test the function
strings = ["a", "b", "c", "abc"]
longest_result = longest(strings)
print("The longest string is:", strings[longest_result])
```