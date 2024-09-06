```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates balanced parentheses from the string and returns the list of their contents.
    """
    list of the open parentheses and their corresponding closed versions are returned.

    Example the balanced set of parentheses.
    """ following regular expression, the balanced set of parentheses are:
    `( )`, `())`, `(( ) )`, `()()`, `(( ) )()`. 110`, `( )`, `())`

    A set of characters that are not balanced are: `( )`, `( )( )`, `( )()`, `(( ) )`, `( )()`, `( )()`, `(() )`
    """
    return [ parent for parent in parentheses if parent != '(' and parent != ')(' and parent != '()' and parent != '(() )' ]
```
This function takes a string of parentheses as an argument and returns a list of all the non-empty parentheses, with their corresponding balanced versions.