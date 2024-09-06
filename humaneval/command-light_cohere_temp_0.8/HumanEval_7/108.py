The Python script provided defines a function `filter_by_substring` that filters a list of strings based on containing a given substring. 

The function takes two parameters: the input list of strings and the substring to search for. The function returns a list of strings that contain the given substring. 

The comments and the docstring are also well-contained and provide a clear explanation of the function's purpose and usage. 

Here's the provided code: 
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if string.contains(substring)]
``` 
The code is self-contained and provides a solution to the problem stated.