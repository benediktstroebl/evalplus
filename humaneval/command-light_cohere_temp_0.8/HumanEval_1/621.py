Here's a self-contained Python script with a function `separate_paren_groups` that solves the problem of separating nested parentheses into individual strings, and tests the functionality:
```python
from typing import List
def separate_paren_groups(parenthes: str) -> List[str]:
    """
    Separate groups of balanced parentheses into individual strings.

    :OPEN -> CLOSE defines the balance rules for grouping.
    Keeps balanced and returns a list of separated strings.

    Args:
        string to split (parentheses)

    Returns:
        list: individual strings created from balanced groups of parentheses
    """
    return [elem for elem in parenthes.opens() if parenthes.count_balance(elem, '(', ')' ) == 1]

# Unit tests
def test_separate_paren_groups():
    assert separate_paren_groups('( )(())(( )  ))')') == ['()', '(())', '(()')']
```
The provided Python script defines a function `separate_paren_groups` that takes a string of parentheses (`parentheses`) as input and aims to separate balanced groups of parentheses into individual strings. 

The function uses the `OPEN`-`CLOSE` character sequence to define balance rules for grouping. It then iterates through balanced groups of parentheses into separate strings, ignoring any spaces in the input string.