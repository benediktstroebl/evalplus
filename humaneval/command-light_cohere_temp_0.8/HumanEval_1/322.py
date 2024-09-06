```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates each group of parentheses into individual strings.

    Input:
    string containing multiple groups of nested parentheses.
    Return: A list of separated strings.

    Test case:
        Simple test with a sample string that contains balanced parentheses.
    """ 
    test_group = ')'
    assert separate_paren_groups(')' == ['')
    test_string = '((()))'
    test_list = separate_paren_groups(test_string)
    assert test_list == ['()', '()']
    test_string_complex = '((()))( )()()()'
    test_list_complex = separate_paren_groups(test_string_complex)
    assert test_list_complex == ['()', '()()()()']
    return test_list_complex
```