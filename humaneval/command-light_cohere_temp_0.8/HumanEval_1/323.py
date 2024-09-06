Here's the Python code with the `separate_paren_groups` function along with the corresponding test cases:
```python
from typing import List

def separate_paren_groups(parenthes: str) -> List[str]:
    """
    This function is designed to separate multiple groups of nested parentheses into separate strings.

    >>> Return a balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the string
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [p.replace('(', ')', end='') for p in parentheses.map() for i, j in range(parenthes) if j == '(']

# Test cases
parentheses = """( ) ( ()( ) ) ( ) ( ) (( ) )"

    assert separate_paren_groups(parentheses) == ['()', '(())', '(()())']
```

This code defines a function to separate balanced groups of parentheses from a given string. It also provides test cases to test the function with different strings.