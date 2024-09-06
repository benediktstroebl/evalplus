The Python script below introduces a function **`filter_by_substring`** that efficiently filters an input list of strings based on a given substring.

- The function employs list comprehension and the **`contains`** method to achieve this, resulting in a concise and clear solution.

```python
import typing

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]
```

This function is straightforward and avoids the use of lists of tuples, which can be beneficial for readability and maintainability in large codebases. 

The explanation for each line of code is provided for better clarity.