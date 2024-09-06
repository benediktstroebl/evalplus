```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    return [pair.format(part, '(')') for pair, part in zip(parentheses, (', '.join(part) for part in parenthesis), ''))]
# Tests
parentheses = ['()', '((()))', '( )', '((((())))))', '(  )', '  (( ()) ) )  ', '((()()))', '( )', '  ( )()' ]
assert separate_paren_groups(parentheses) == ['(), (())', '(()())', '()', '( )', '((())', '(()())']
```