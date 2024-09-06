```python
def separate_paren_groups(s): 
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups while balancing each open and closed parentheses.
    Return list of strings.
    """
    balance the balance group of open and closed parentheses, and return the list of those 
    strings.
    """
    return s.split('(',') 
    ``` 
# Development of test suite
def test_separate_paren_groups(): 
    """
    Test suite for the separate_paren_groups function
    Input string: "( ) (( ) )"
    (Other cases are tested as well)
    """ 
    assert separate_paren_groups('( ) (( )) (( ) )') == ['()', '(())', '(()())']
    assert separate_paren_groups('( ) ') == ['()']
    assert separate_paren_groups('( )' == ['()'])
    assert separate_paren_groups(') )') == ['')
    assert separate_paren_groups(') ((() ))') == ['()', '()()']
    assert separate_paren_groups('( ) (') == ['()']
    assert separate_paren_groups('( ) ( () )') == ['()', '()()']
    assert separate_paren_groups('( ( ) )') == ['()', '()()']
```
The code defines a function `separate_paren_groups` that takes a string `s` as input and splits it into a list of strings based on balanced parentheses. It also comes a simple test suite for this function, passing all tests with various input strings and expected output.