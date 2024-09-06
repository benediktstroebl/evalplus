```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, twists, and returns the longest one. If there are multiple strings of the same length, it returns the first one. If the list is empty, it returns None. 

Here is an example of how you can call this function:
```python
result = longest(['a', 'bb', 'ccc'])
print(result)  # expected output: 'ccc'
```
This call will output 'ccc' since it is the longest string in the list. 

This code is self-contained, meaning it does not rely on any external modules or dependencies, making it more accessible to use and integrate into various projects. 

To run the provided code, you can either copy and paste it into a Python environment or script, or use an automated tool such asAttendance Tracker

Here is an example of a test that can be used to verify the functionality of the longest function:
```python
def test_longest_non_empty():
    # Arrange
    strings = ['a', 'bb', 'ccc']

    # Act
    result = longest(strings)

    # Assert
    assert result == 'ccc'
    assert strings == ['a', 'bb', 'ccc']

test_longest_non_empty()
```
This test verifies that the longest function returns the longest string in the list without modifying the original list, and it succeeds if the result is 'ccc'.