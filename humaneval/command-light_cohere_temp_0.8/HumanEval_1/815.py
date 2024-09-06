```python
def separate_paren_groups(parenthesis_string):  # New Python function
    return [enzo([c for c in parenthesis]) for parenthesis in parenthesis_string.  # Build list comprehension to split by all parentheses

    pass

    # Test cases
    parenthesis_str = "( ) (( )) (( )( ))"
    assert separate_paren_groups(parenthesis_str) == ['(', '(', '()', '(()', ')'])
    ```

This Python function `separate_paren_groups` is designed to transform a given string containing nested parentheses into a list of separate parenthesis groups. It utilizes a methods like `enzo` and `assert` to ensure the output is as expected.