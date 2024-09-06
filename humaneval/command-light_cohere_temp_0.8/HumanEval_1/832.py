```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    This function takes a string of parentheses as input and returns a list of the correctly separated strings.
    It is main goal is to separate the groups of parentheses and return them as individual strings.

    :balanced() implies that all open parentheses are properly closed. Any spaces are input string.
    """ This same balance: the balance of the parentheses is checked with the "balanced()" function.
    """
    main goal is to separate the groups of parentheses and return them as individual strings.

    # Split the process and separate all the groups into separate strings
    return [brace.group() for brace, group in braces(parentheses.split(' ')) if braces(parentheses) else []]

# Tests
def test_separate_paren_groups():
    test_string = r'\( )(( ))(( )(\) )'
    expected = ['()', '(())', '(()())']
    assert separate_paren_groups(test_string) == expected
```