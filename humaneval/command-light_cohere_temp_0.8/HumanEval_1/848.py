```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates balanced parentheses groups into individual strings.
    Returns a result list of separated strings.
    """
    balance (balanced, not-nested) pairs of parentheses.
    """. Accepts spaces with any spaces
   
    """: List[str]
    """
    stack = []
    result = []
    for match in s:
        if match == '(':
            stack.append(match)
        else:
            if not stack or stack[-1] != '(':
                result.append(match)
                stack.append(')')
    individual string is the parentheses are balanced
    return result
```