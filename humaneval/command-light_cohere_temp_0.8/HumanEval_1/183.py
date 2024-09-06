```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate different groups of opening parentheses from a given string.
    Returns a certain list of opening parentheses separated by their own balances.
    """

    Input to this function is a string containing multiple groups of nested parentheses.
    Returns: list of separated opening parentheses.
    """
    example usage:
    ```
    s = '() (( )) (( )( ))'
    opening_paired = separate_paren_groups(s)
    print(opening_paired)
    # ['(', ')', '(', ')', '()']
    ```