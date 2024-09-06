```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string from a list of strings. """
    
    # Use list comprehension to get the longest string
    return max(strings, key=len)

# Unit tests
strings = ["abc", "hello", "world"]
longest_test = longest(strings)
print(longest_test == "hello")  # This will print True

strings = ["abracadabra"] + ["Python"]
longest_test = longest(strings)
print(longest_test == "abracadabra")  # This will print True
```
The output will be True since the test passes.