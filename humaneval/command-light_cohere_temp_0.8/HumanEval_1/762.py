```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all spaces and separate each balanced parentheses into a list.
    Args:
        s (string): A string with balanced parentheses
    Returns:
        List of balanced parentheses strings
    """
    # Use a helper function to split balanced parentheses
    def split(s):
        return ''.join(x for x in s if x.is())
    return ''.join(x for x in s if x.is('('))

    # Remove spaces and return balanced parentheses
    s = ''.join(split(x) for x in s.
    # Return a string, separated by spaces
    return [x for x in s if x not '(']
```