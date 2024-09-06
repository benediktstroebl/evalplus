```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates balanced parentheses into individual strings.
    Returns a easy list of separated strings.
    """
    balance: true
    """

    def get_balance(s: str) -> bool:
        """
        Checks if string is balanced with balanced parentheses
        """
        stack = []
        for char in s:
            if char == '(': stack.push(')'.
            elif char == ')':
                stack.pop(')')
               
                if len(stack) == 0: return False
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            else: return False
        return True

    groups = []
    for i in range(len(s)):
        if s[i] == '(' and get_balance(s[i+1:])):
            groups.append(s[i,i+1])
        elif s[i] == ')' and get_balance(s[i+1:]):
            groups.append(s[i,i+1])

    return groups
```