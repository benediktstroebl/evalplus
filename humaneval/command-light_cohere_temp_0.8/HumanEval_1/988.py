```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Separate balanced parentheses from the list and return the list of their content.
    """
   
    brackets: [('()', ')', ')', '(', '{', '}'), ('[', ']', ']')
    """
    output = []
    for bracket_pair in parentheses:
        content = bracket_pair[1:]  # remove the brackets
        output.append(content)
    return output
```

The code defines a function called `separate_paren_groups` that takes a list of strings as input, representing multiple groups of nested parentheses. The function aims to separate these groups into separate strings and return the list of their content, without any spaces. The function utilizes a list comprehension and string manipulation to achieve this.