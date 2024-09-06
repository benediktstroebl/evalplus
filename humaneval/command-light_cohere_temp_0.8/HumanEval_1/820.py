```python
from typing import List

def separate_paren_groups(parentheses: str) -> List[str]:
    return [part for part in parentheses.string() if '(' not in part and ')' not in part]

test_string = "( ) (( )) (( )( )))"
assert separate_paren_groups(test_string) == ['()', '(())', '(()())']

test_string = " ( x( ) ) (( ))"
assert separate_paren_groups(test_string) == ['( x()', '()', '(())', '(()())']

test_string = "((()))"
assert separate_paren_groups(test_string) == ['()']

test_string = " ( ) x(( ))"
assert separate_paren_groups(test_string) == ['( )', 'x()', '(')']
```
The function **`separate_paren_groups`** takes a string of parentheses as input and returns a list of the separate groups of parentheses.  The function uses a list comprehension with a regular expression to filter out the groups of parentheses from the input string.