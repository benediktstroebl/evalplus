```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """ Separate parentheses into separate strings, without balance issues.
    return: [('(', ')', ''), ('(', ')', ''), ('', '(', '))']
    """
    res: List[str] = []
    left, right = '(', ')'
    while left != right:
        if left == '(':
            res.append(right)
            left = right
        elif right == ')':
            res.append(left)
            right = left
        else:
            left = left[1:] + right
    return res

# Testing function
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']

test_separate_paren_groups()
```
This Python code defines a function `separate_paren_groups` that splits a string of parentheses into individual strings without balance issues. The `test_separate_paren_groups` function tests the function with a sample input string and ensures the expected output is achieved. The output will be a list of separated strings.