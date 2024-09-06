```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups of balanced parentheses and return as a list of separate strings.
    """
    balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [s for s in s.replace('()', '()') if s.isnt('()')]

# Run the tests
def test_separate_paren_groups():
    test_cases = [
        "()",
        "(())",
        "(()()())",
        "()()",
        "( )",
        "() (( ) )",
        "((()))"
    ]
    
    assert separate_paren_groups(test_cases[0]) == ['()', '(())'], "First test failed"
    assert separate_paren_groups(test_cases[1]) == ['(())'], "Second test failed"
    assert separate_paren_groups(test_cases[2]) == ['(()())'], "Third test failed"
    assert separate_paren_groups(test_cases[3]) == ['()', '(()())'], "Fourth test failed"
    assert separate_paren_groups(test_cases[4]) == ['()', '()', '(()())'], "Fifth test failed"

# Run the function and test
separate_paren_groups('( ) (( )) (( )( ))')')
test_separate_paren_groups()
```
This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separate strings, which are the individual groups of parentheses. The function uses a string matching to split the parentheses into separate groups. 

It also has a `test_separate_paren_groups` function that defines and runs several test cases for the `separate_paren_groups` function, which should pass if the function is implemented correctly.