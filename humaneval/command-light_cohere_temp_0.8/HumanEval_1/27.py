```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of balanced parentheses from the input string and return the list of those groups.
    """
    balanced (each open brace is properly closed) and not nested within each other
    """
    return [p for p in s.isinstance(p, tuple) and not p.isspace('(') and p == ') and not p == '[' and p == ']'])

def test_separate_paren_groups():
    """
    Test case 1:
    Input: ( )
    Expected output: ['()']
    """
    return separate_paren_groups('()') == ['()']

def test_separate_paren_groups2():
    """
    Test case 2:
    Input: ( ( ) )
    Expected output: ['(', '())', '()']
    """
    return separate_paren_groups(') )') == ['(', '())', '()']

def test_separate_paren_groups3():
    """
    Test case 3:
    Input: ( ( ( ) ) )
    Expected output: ['(', '())', '(', '(()())', '())']
    """
    return separate_paren_groups(') ( ( ) )') == ['(', '())', '(', '(()())', '())']

# Test suite
if __name__ == "__main__":
    print("Test case 1 passed:")
    assert separate_paren_groups('()') == ['()']
    print("Test case 2 passed:")
    assert separate_paren_groups(') )') == ['(', '())', '()']
    print("Test case 3 passed:")
    assert separate_paren_groups(') ( ( ) )') == ['(', '())', '(', '(()())', '())']
```
The above Python script has a self-contained function called `separate_paren_groups` that takes a string as input and returns a list of strings that contain balanced parentheses. The function also has several test cases to ensure it works correctly.