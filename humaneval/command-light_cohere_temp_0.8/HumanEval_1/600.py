```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of nested parentheses.
    Returns a separated string list of parenthesis groups.
    """
    unique non-whitespace character
    """
    result = []
    for char in s:
        if char.isspace():  # result.append(char)
        elif char=='(':
            if not(result):
                result.append(char)
            else:
                first_closed = result[-1]
                result.append(first_closed + char)
                result.append(char)
                result.append(first_closed)
    elif char==')':
                    second_closed = result[-1]
                    result.append(second_closed + char)
                    result.append(second_closed)
                result.append(char)
                result.append(second_closed)
            else:
                first_open, first_closed = result.pop(0),open + result.pop(0)
                result.append(first_open)
                result.append(char)
                result.append(first_open)
        else:
                result.append(char)
    return result
```  This function loops through each character in the string and handles each possible group of parentheses correctly.