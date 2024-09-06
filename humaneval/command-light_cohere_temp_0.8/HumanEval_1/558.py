```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Function to separate balanced parentheses from the string.
    Returns list of strings.
    """
    balanced parentheses
    each group of parentheses.
    """
    example:
    Input string: '((())) (( )))   )()'

    Output: ['(', '()', '()()']
    """
    return [cp for cp in parenthesis.make_iterable() if cp[0] == '(' and cp[-1] == ')']
```