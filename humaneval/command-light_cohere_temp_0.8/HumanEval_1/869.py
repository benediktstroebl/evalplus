```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    Separate and return parenthesis groups in an input string.

    :string -> Input string
    balanced (each open brace is properly closed) and not nested
    """
    # Create list of substrings.
    substrings = []
    for match in input_string.match('\([.*?MODBERICOSP(.*])'):
        substrings.append(match.group(match)[1:-1])
    # Group may contain other operators too.
    return substrings
 return [] # Test cases are not added
```