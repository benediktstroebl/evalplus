Here's a self-contained Python function that splits a string of parentheses into a list of separate groups:
```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates a string of parentheses into individual groups.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [pi.strip() for pi in parentheses.split('\\('+')]
```
This function takes a string of parentheses as input and returns a list of separate groups of parentheses. It uses the regular expression to split the string of parentheses into a list of parentheses, which are then transformed into a list of strings using the `map()` function.