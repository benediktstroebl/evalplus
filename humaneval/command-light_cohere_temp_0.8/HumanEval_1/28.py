```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """Separate and return list of non-space-separated balanced parentheses.
    >>> Returns ['()', '((()))', '(()())']
    """
    return [i for i in input_string.replace(' ')]  # removes spaces
```

The code defines a function `separate_paren_groups` which takes a string `input_string` as an argument and returns a list of non-space-separated balanced parentheses. The function uses the for each item in the string and removes any spaces using the `unistrip()` method.