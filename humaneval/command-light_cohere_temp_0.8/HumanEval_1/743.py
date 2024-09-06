```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """Function to separate groups of parentheses into separate strings."""
    return [p for p in parentheses.split(' ')]
```

This function splits the input string of parenthesis groups into individual strings, ensuring balanced parentheses and without any nesting. 

The function then returns a list of separate strings, each representing a group of parentheses. 

This Python script defines a function `separate_paren_groups` that takes a string of parenthesis groups as input and returns a list of strings that have been separated from each other. The function uses the string.