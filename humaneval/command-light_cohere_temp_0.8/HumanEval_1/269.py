```python
from typing import List
def separate_paren_groups(parenthesis_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses into separate strings.
    Returns a balanced (each open brace is properly closed and not nested within each other)
    """
    result = []
    stack = []
    for char in parenthesis_string:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] != '):':
                result.append(stack.pop()
               
               
            open parentheses.
    return result

    test_cases = [
        ("()", "(())"),
        ("( )", "( )()"),
        ("()", "( )()"),
        ("( )", "(  )"),
        ("()()", "()"),
        ("()()()", "()()"),
        ("( )()", "()"),
        ("( )  ", "()"),
    ]
    assert separate_paren_groups(test_cases[0]) == ['()', '(())'], "First test failed"
    assert separate_paren_groups(test_cases[1]) == ['()', '('), "Second test failed"
    assert separate_paren_groups(test_cases[2]) == ['()', '(')'], "Third test failed"
    assert separate_paren_groups(test_cases[3]) == ['()', '()'], "Fourth test failed"
    assert separate_paren_groups(test_cases[4]) == ['()', '()'], "Fifth test failed"
    assert separate_paren_groups(test_cases[5]) == '()', "Sixth test failed"
    return  # empty string as the test passed
```