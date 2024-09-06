```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string in the list """
    if not strings:
        return None
    return max(strings, key=len)

# Test case:
test_strings = ['a', 'bb', 'ccc']
longest_result = longest(test_strings)
print("Longest string:", longest_result)  # Output: "ccc"
```
This code provides a self-contained function `longest`, which takes a list of strings and returns the longest string. The test case demonstrates the use of this function with an example list of strings. The output of this code is the longest string in the list, which is "ccc".