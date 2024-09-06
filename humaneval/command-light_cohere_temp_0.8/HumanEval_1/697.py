```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all parenthesis groups, returns list of inner strings.
    """
   
    not intended to be the fastest function, just simple and clear
    """
    return [item.replace each inner string is result of splitting the full string with  matches of open parenthesis.
    # Modified to work with any spaces between characters and parenthesis.
    """
    print(s, "=>", separate_paren_groups(s))
    assert separate_paren_groups("( ) (( )) (( )( ))")") == ['()', '(())', '(()())']
    assert separate_paren_groups("( )  (( ))")") == ['()', '()()]
    assert separate_paren_groups("(( ))")") == ['()', '()()]
    assert separate_paren_groups("( )  ") == ['()']
    assert separate_paren_groups("  ( )  ") == ['()']
    assert separate_paren_groups("( , )") == ['(', ' )']
    assert separate_paren_groups("( )()") == ['()()']
    assert separate_paren_groups(" ( ) ") == ['()']
    return []
```