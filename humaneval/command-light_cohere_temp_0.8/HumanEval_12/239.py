```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len)

# Test case:
def test_longest():
    return not longest([]) is None  

test_longest()
``` 
This function takes a list of strings and returns the longest string in the list. It uses the max function with the key parameter set to the length of each string in the list. The test case tests if the output of the function is `None` it fails.