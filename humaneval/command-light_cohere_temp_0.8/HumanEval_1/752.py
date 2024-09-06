```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Removes all parenthesis groups, returns as list.
    """
    open, closed ) pairs are brackets.
    """
    remove all spaces,
    """

    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack or stack[-1] != '(':
                stack.append(c)
        else:
                first, last = stack.pop()
                open, closed = stack
                if first != '(' or last != ')' or (first == '(' and last == ')'):
                    raise ValueError("Incorrect format of input string.")
                stack.append(first + '(')')
            else:
                while stack and stack[-1] != '(':
                    stack.pop()
                stack.append(last)
                stack.finally list comprehension is Python provides a list of all the non empty elements in a sequence.
    return [list(filter(lambda x: not.isspace(x), x), not x == '(' or x != ')'
                or x == '(' and x == ')'
                and not x == ')')))
```