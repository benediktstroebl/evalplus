```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from the list of strings.
    Args:
        strings (List[str]): List of strings.
    Returns the string with the maximum length
    """
    if not strings:
        return None

    return max(strings, key=len)

# Unit tests
def test_longest():
    test_list = ['a', 'b', 'c']
    longest_result = longest(test_list)
    assert longest_result == 'a'
    test_list2 = ['a', 'bb', 'ccc']
    longest_result2 = longest(test_list2)
    assert longest_result2 == 'ccc'
```
This Python script defines a function called **longest** that takes a list of strings as input and returns the longest string from that list. The function uses the max function with the **len** key function to determine the length of each string and return the longest one. The function is also tested with two different lists of strings to ensure its correctness.