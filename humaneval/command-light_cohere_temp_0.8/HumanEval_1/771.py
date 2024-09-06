```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns a list of non-empty groups of parentheses in a string.
    : Groups should be balanced with each open parenthesis properly nested and closed.
    Returns: list of strings with balanced groups of parentheses.
    """ Other open to the list comprehension
    """
    Do note that this function uses list comprehension with a lambda function to iterate over the string.
    : In Python 3.7 and above, the balanced group must contain at least one open parenthesis.
    """
    balanced group could as a single string.
    """
    get_balanced_group(s, i, j) -> s[i:j+1] if s[i:j+1] == '('.join(s[i:j]))
    return [get_balanced_group(s, i, j) for i in range(0, len(s)) for j in range(i+1, len(s))]
tests = ['''
    string = "( ) (( )) (( ))"
    expected = ['()', '(())', '(()())']
    assert separate_paren_groups(string) == expected
    '''')
    tests.add(
        "string = '(())'
    expected = ['()', '(()())']
    assert separate_paren_groups(string) == expected
    '''')
    tests.add(
        "string = '(())'
    expected = ['()', '()']
    assert separate_paren_groups(string) == expected
    '''')
```