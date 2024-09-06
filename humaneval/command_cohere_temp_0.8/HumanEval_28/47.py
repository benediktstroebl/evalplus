```python
# Markdown code block
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for string in strings:
        result += string
    return result
```
The `concatenate` function takes a list of strings (`List[str]`) as an argument and returns a single string that concatenates all the strings in the list. It achieves this by iterating through each string in the list and adding it to a running result string. The function is tested with empty and non-empty lists, and the expected concatenated results are returned accordingly. 
The description of the function also includes doctests that allow you to verify the function's behavior directly in the Python script. 
The markdown code block containing the Python script provides a comprehensive solution to the problem and demonstrates the usage of the `concatenate` function with example tests.