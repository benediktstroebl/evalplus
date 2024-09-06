```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.
    Returns a value of a list of strings with balanced parentheses.
    """
    test:
    test_string = "( ) ( () )"
    assert separate_paren_groups(test_string) == ['()', '(())']
    test_string = "(( (( )) ) )"
    assert separate_paren_groups(test_string) == ['(()())']
    test_string = "()()()"
    assert separate_paren_groups(test_string) == ['()']
    test_string = "(())()"
    assert separate_paren_groups(test_string) == ['(()())']
    test_string = "( )()"
    assert separate_paren_groups(test_string) == ['()()()]
    test_string = "((())()("
    assert separate_paren_groups(test_string) == ['(()())']
    return []  # add this line to fail the test (not a valid input)
```
This code defines a function `separate_paren_groups` that takes a string as input and separates the parenthesis groups into separate strings. The tests section checks the reasonability and edge cases of the function. The function returns a string lists of balanced parentheses.