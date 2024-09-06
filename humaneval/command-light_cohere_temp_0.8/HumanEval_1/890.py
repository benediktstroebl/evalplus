```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates a string of parenthesis groups into individual strings.
    Each individual has balanced and properly nested parentheses.
    Returns list of strings.
    """
   
    might be used to verify the function's correctness.
    """
    The string is split into individual strings, without any nested parentheses or spaces.
    """:return [ s.sub.replace(r"\",tuple('('(') for r in s if r=='))
    for _ in range(len(s)-1) ]] ]

# Example function call
test_cases = [
    '() (( )) (( )( ))',
    '( )',
    '()()',
    '((()))',
    '() ( )'
]

print(separate_paren_groups(test_cases))
```