Here is a self-contained Python script that defines a function `separate_paren_groups` solving the problem you described:
```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Input is a list of strings containing parentheses. Separate groups into balanced parentheses into a list and return the list of those separated strings.
    """
    open_parens = set()
    output_parens = []
    for par in parentheses:
        if par[0] in open_parens:
            open_parens.append(par[1])
        else:
            open_parens.append(par)
        output_parens.append(par[2:])
    return output_parens
```