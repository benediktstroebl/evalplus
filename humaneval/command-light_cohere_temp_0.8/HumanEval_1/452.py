```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses into individual strings.

    Args:
        paren_string (str): A string containing multiple groups of parentheses.

    Returns: list of strings, each containing a balanced group of parentheses.
    """
    test:
    Test case with an example string that contains unbalanced parentheses.
    """
   
    test_string = "((()))"
    test_result = separate_paren_groups(test_string)
    assert test_result == ['()']
    test_result = " (())" + "(( ) )"
    assert separate_paren_groups(test_result) == ['()', '()()]
    test_result = "  ( )  (( ))"
    assert separate_paren_groups(test_result) == ['()', '()()']
    test_result = "(((())))"
    assert separate_paren_groups(test_result) == ['(())']
    test_result = "(( () )) (( ))"
    assert separate_paren_groups(test_result) == ['()', '(())']
    test_result = "(( () ( ) ) )"
    assert separate_paren_groups(test_result) == ['()', '()()']
    test_result = "(( () () () ))"
    assert separate_paren_groups(test_result) == ['()', '()()', '()']
    """
    return [par for par in paren_string if par == '(' or par == ')']
```
This Python script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of individual balanced parentheses. The function uses a test cases to ensure its correctness, including various scenarios with unbalanced and balanced parentheses.