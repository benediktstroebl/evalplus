```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates groups of balanced parentheses from the input string.

    >>> separated_paren_groups('( )((())))
    ['(', ')', '()()']
    """
    # Use a helper function to check if a string is balanced
    def is_balanced(s: str) -> bool:
        opening, closing = '(', ')'
        return opening == s.find(closing) and closing in s.
        return False
     # Balanced input!
    # Remove all unbalanced groups and keep balanced ones as separate strings
    groups = [s for s in parenthesis if is_balanced(s)]
    return groups

# Run tests on the function
parentheses = '( )((()) )'
assert separate_paren_groups(parentheses) == ['(', ')', '()()']
```