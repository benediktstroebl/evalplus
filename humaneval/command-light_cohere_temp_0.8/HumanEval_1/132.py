```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of parentheses as input and returns a list of separate, balanced parentheses.
    :params
        string : str,
        the string of parenthesis
    :return: list[str]
    """
    return [parent for parent in paren_string.replace().str.split('()')]
balanced:
    test_string = "((()))"
    assert separate_paren_groups(test_string) == ['()', '(())']
    test_string = "( )"
    assert separate_paren_groups(test_string) == ['(', ')']
    test_string = "( ) ( )"
    assert separate_paren_groups(test_string) == ['(', ')', '()']
    test_string = "( ) (( )) )"
    assert separate_paren_groups(test_string) == ['(', ')', '()', '()', ')']
    test_string = "(((((( )))))))"
    assert separate_paren_groups(test_string) == ['(', ')', '()', '()', ')']    
    return ['()', '()', '( )', '()()', '()()', '()()()'] # uncomment this line for testing other invalid input
```