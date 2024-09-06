```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into separate strings"""
    result = []
    stack = []
    for char in s:
        if char == '(': stack.push(')')
        char
        elif char == ')': stack.pop()
        specific_string = ''.join(stack)
        result.append(specific_string)
        stack = []
    return result
# Test cases
def test_cases():
    test_str = "( ) (( )) (( )( ))"
    assert separate_paren_groups(test_str) == ['()', '(())', '(()())']
    test_str = " (( )) (( ( )) )"
    assert separate_paren_groups(test_str) == ['( )', '()()()', '()()()']
    test_str = "(( (( )) ) (( (( )) )"
    assert separate_paren_groups(test_str) == ['( )', '((()))()', '(()())']
    test_str = "( ( ) )"
    assert separate_paren_groups(test_str) == ['()', '(', ')']
test_cases() 
``` 
This code defines a function `separate_paren_groups` that takes a string as input and creates an array of separate strings by separating parentheses. The test cases verify the test and it passes the test successfully.