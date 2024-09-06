Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```
This script defines a function `longest` that takes in a list of strings `strings` as input and returns the longest string in the list. If there's only one string in the list, or if all strings in the list have the same length, it returns the first string using the `or` clause in Python. It employs the `typing` module for type hints as well. 

Here is an example usage of the function with a test:
```python
def test_longest():
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest([]) is None
    assert longest(['a', 'b', 'a']) == 'a'
```

This uses Python's `assert` statement to check whether the function's output agrees with its expected output for each of the test cases. 
The function `longest` handles the corner cases where the list might be empty or might have strings of the same length, and it returns the longest string from the list. 

The script ensures the function behaves as expected and effectively provides a self-contained solution to the problem.  In this case, the function is standalone and does not require any additional dependencies or modifications to the testing framework itself.