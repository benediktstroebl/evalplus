```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate each group into balanced parentheses and return as a list.
    >>> ['()', '((()))', '(()())']
    """
    return [part for part in input_string.split('()')]
```
This Python function called `separate_paren_groups` takes a single argument `input_string`, which is expected to contain multiple groups of balanced parentheses. 

The function uses the `split` method on the `input_string` to create separate substrings for each group. Then, it creates a list `parts` and populates it with elements from each of these substrings.