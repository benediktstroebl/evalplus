```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings.
    """
    balanced (each open brace is properly closed) and not nested within each other.
    Returns a accepted input string of balanced parentheses.
    """
    test cases:
    - Blank string
    - Open parenthesis only
    - Close parenthesis only
    - Both open and close parenthesis
    - Multiple balanced groups
    """
    stack: List[str] = []
    for char in parentheses:
        if char == ')':
            stack.append(')')
        if stack else:
                return stack.stack.append(char)
        if char == '(':
                stack.append(char)
                if stack else:
                    return stack
    return []

def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'])')
    assert separate_paren_groups(' )') == [''])
    assert separate_paren_groups('( )') == ['()'])
    assert separate_paren_groups('( )( )') == ['(', '()', ')'])
    assert separate_paren_groups('((( ))))') == ['()', '((()))')']
    assert separate_paren_groups('( )( )')) == ['(', '()', ')')
```
This script defines a function **`separate_paren_groups`** that takes a string of balanced parentheses as input and returns a list of individual strings that each represents a balanced group of parentheses. The **`test_separate_paren_groups`** function tests the function with various inputs and asserts the correct output for each case.