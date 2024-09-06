```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string in a list, or None if empty """
    return max(strings, key=len) or None

# Unit tests for longest function
def test_longest() -> None:
    """ Assert that the longest function returns the correct value """
    strings = ['a', 'bb', 'ccc']
    assert longest(strings) == 'ccc'
    strings = []
    assert longest(strings) is None
    strings = ['a']
    assert longest(strings) == 'a'
    return

if __name__ == "__main__":
    test_longest()
``` 
This code contains a function `longest` which takes a list of strings and returns the longest string in the list, or `None` if the list is empty. It uses the `max` function with a custom key to compare strings by length and returns the longest. 

The test cases for this function ensure that it works correctly with different input scenarios.