```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string containing multiple groups of parentheses and returns a list of separate, balanced parentheses.
    Balanced according to the standard [https://en.ooo.punctuation.ly.into balanced parentheses.
    """ 

     The number of balanced parentheses and their spaces are:
    """
    balance = 0
    parentheses = []
    for i, char in enumerate(s):
        if char == ' ':
            balance += 1
        elif char == ')' and balance > 0:
            balance -= 1
            parentheses.append(char)
        elif char == '(' and balance > 0:
            balance -= 1
            parentheses.append(')')
        elif char == '(' and balance < 0:
            balance += 1
            parentheses.append('(')
        else:
            pass
    return parentheses
```