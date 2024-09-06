```python
from typing import List
def separate_paren_groups(parenthesis_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses into individual strings.
    """
    balance ( balanced or unbalanced ) parentheses.
    """
    balanced: open and close parentheses in order from left to right.
    unbalanced: leave only the unbalanced ones
    """
    @return list of strings
    """
    result = []
    stack = []
    for char in parenthesis_string:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                result.append(''.join(stack))
                stack = []
    return result
# Tests
def test_separate_paren_groups():
    test_cases = [
        "()(( ))(( )( ))'
    ,"  )((  ))"
    ,'()((  )())'
    ,"( )"
    ,'()()())"
    ,'( ) )()'
    ]
    assert separate_paren_groups(test_cases[0]) == ['()', '(())', '(()())']
    assert separate_paren_groups(test_cases[1]) == ['()', '(())', '(()())']
    assert separate_paren_groups(test_cases[2]) == ['()', '(()')]
    assert separate_paren_groups(test_cases[3]) == ['()', '()()()]
    assert separate_paren_groups(test_cases[4]) == ['()', '()()()']
    assert separate_paren_groups(test_cases[5]) == ['(', ')']
```