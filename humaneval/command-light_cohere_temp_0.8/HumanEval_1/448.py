```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Separate groups of balanced parentheses into separate strings.

   balanced = [ [ ([('()', '('), '()'), ('()', '('))], [], ['()', ')'])
    test_cases = [
        '()', '( )', '() ()',
        '( )()',
        '(() )()',
        '(() ()()',
        '() ()() ()',
        '() ( ) ()',
        '(  )'
    ]

    return [match for match, _ in balanced]
```