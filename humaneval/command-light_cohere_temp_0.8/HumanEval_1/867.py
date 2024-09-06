```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates balanced parentheses into individual groups.
    Returns list of strings. Each string represents a unique group of balanced parentheses.
    """:
        Each group of parentheses are balanced.
    """:
        {  [('(')(')'))
            ,'')
            ,'()')
            }
    """
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                result.append(''.join(stack))
                stack.clear()
        stack = []
        else:
            stack.append(char)
    else:
        pass 
    
    return result

# Test the function
def test_separate_paren():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
test_separate_paren()
```
This script defines a function named `separate_paren_groups` that splits a string of balanced parentheses into individual groups, and a function `test_separate_paren` that tests the correctness of this function.