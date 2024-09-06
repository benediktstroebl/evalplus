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
This script defines a function `longest` that takes in a list of strings `strings` as input and returns the longest string in the list. If there's only one string in the list, or if all strings in the list have the same length, it returns the first string using the `or` clause in Python. It employs the `max` function with a custom key specified using the `key` argument to return the longest string in case of multiple strings of different lengths.

To check the functionality of this solution, you can test it using the following Python code:
```python
# Test 1
assert longest([]) is None

# Test 2
assert longest(['a', 'b', 'c']) == 'a'

# Test 3
assert longest(['a', 'bb', 'ccc']) == 'ccc'
``` 
This tests the function on the three specific cases mentioned in the prompt.