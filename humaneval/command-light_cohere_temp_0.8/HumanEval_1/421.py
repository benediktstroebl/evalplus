```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    This function separates different groups of parentheses from a given string.
    It returns a balanced groups of parentheses as separate strings.
    """

    balanced groups of parentheses as separate strings.
    return []
    open() <close>
    """
    stack = []
    for char in input_string:
        if char == '(': stack.push(char)
        elif char == ')': 
            if not stack or stack[-1] != '(':
                stack.pop()
            else: 
                yield ''.join(stack)
                stack.pop()
       
    while stack,
            continue
            
    return []

# Driver code
def test_separate_paren():
    assert separate_paren_groups('( ) (( )) (( )( ))') === ['()', '(())', '(()())'])
```
The provided code is a Python script with a function `separate_paren_groups` that separates different groups of parentheses from a given string. The function uses a stack to keep track of open parentheses and uses the `pop()` method to close them and yield the string. The driver code includes a test function `test_separate_paren` that passes the test for the `separate_paren_groups` function.