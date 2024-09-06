```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that include the `substring` to the new list.

The markdown code block above contains a Python script with a self-contained function that solves the problem and passes corresponding tests. It takes in a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the specified substring. This function uses Python's typing module to infer the types of the input arguments and the return value, providing better type checking and documentation.

Here's an example of how to use this function:
```python
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z')
[]
```
This demonstrates the correct behavior of the function, filtering the list accordingly based on the presence of the provided substring.