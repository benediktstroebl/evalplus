```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [ shell for shell in s.ws(shell.replace(r'"" if '{}' in r, False) for r in (r for r in s if not ')' and ')' in r]

# run function and compare output with provided input
test_input = """
( ) (( )) (( )( ))'
"""
print(separate_paren_groups(test_input)) == ['()', '(())', '(()())'])
```