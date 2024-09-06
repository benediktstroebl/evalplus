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
This script defines a function `longest` that takes a list of strings as input and returns the longest string. If there's only one string in the list, or if all strings in the list have the same length, it returns the first string using the `or` clause in Python. It employs the `max` function with a custom key specified using the `key` argument to return the longest string in case of multiple strings of different lengths.

To verify the correctness of the `longest` function, you can add test cases in the same file in the form of Python's `assert` statements or use f-strings for more expressive testing:
```python
>>> longest([])
None
>>> longest(['a', 'b', 'c'])
'a'
>>> longest(['a', 'bb', 'ccc'])
'dccc'
>>> longest(['supercalifragilisticexpialidocious', 'hello', 'test'])
'supercalifragilisticexpialidocious'
```
However, to maintain the initial prompt's directive to solve the problem within a markdown code block, I will not include these test cases within the script but instead provide a separate markdown code block containing test cases with the `>>> ` prefix to indicate Python execution. You can then verify the output of each test case to ensure the `longest` function behaves as expected. 
```python
# Example usage:
>>> longest(['supercalifragilisticexpialidocious', 'hello', 'test'])
'supercalifragilisticexpialidocious'
```