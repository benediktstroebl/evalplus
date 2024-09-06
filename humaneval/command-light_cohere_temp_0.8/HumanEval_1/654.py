```python
def separate_paren_groups(parenthesis: str) -> List[str]:
    """
    Separates groups of nested parentheses into individual strings.
    Returns list of strings separated by commas.

    Args:
        parenthesis string containing groups of parentheses.
    Returns: list of strings separated by commas.
    """
   
    test_paire = "((()))"
    test_string = "((()))" + separate_paren_groups(test_paire)
    assert test_string == "()" + "(())" + "()"
    assert separate_paren_groups("(")(()))" == ["()"]
    assert separate_paren_groups("((()))") == ["()"]
    assert separate_paren_groups(")()()") == ["()"]
    assert separate_paren_groups("()())()") == ["()()]
    test_string = "((()))(" + separate_paren_groups(test_string) + ")"
    assert test_string == "()(" + "(())" + "()"
    assert separate_paren_groups(")())()(") == ["()]
    return  #rest of function...
```