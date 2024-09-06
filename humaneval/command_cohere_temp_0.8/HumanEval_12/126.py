```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script provides a function called longest as per your prompt, taking a list of strings as an argument and returning either None, or the longest string if the list contains at least two strings. The function checks if the list is empty, or if there is only one unique string in the list, and returns None and the singular string, respectively. If there is more than one string, the function employs the max function, specifying the len function as the sorting key to return the longest string and handles multiple strings of the same length by selecting the first one. 

Here is an example of how to use this function:
```python
print(longest(['a', 'bb', 'ccc']))
```
This will print out `ccc` as the output, which is the longest string in the list ['a', 'bb', 'ccc']. 

Below is a basic test suite with an `assert` statement to verify the function behaves as expected: 
```python
def test_longest():
    # None for empty list
    assert longest([]) is None
    # Single string
    assert longest(['a']) == 'a'
    # Longest string
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    # Handling equal lengths
    assert longest(['ab', 'bc']) == 'ab'
```
You can use this basic test suite to validate the function further if needed. It is important to note that this is a simple test suite and may not cover all edge cases for the function.