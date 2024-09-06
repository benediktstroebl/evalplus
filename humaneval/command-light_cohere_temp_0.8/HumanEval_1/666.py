```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns a list of parenthesis groups.
    The opening and closing parentheses are '(', ')'
    """
    return [c for c in s if c == '(' or c == ')']

# Test string with different cases
tests = """
md_code = '() (( )) (( )( ))'
other = " function"
string = " Hello World. Are you ready for anything" "
print(separate_paren_groups(md_code))
print(separate_paren_groups(other))
print(separate_paren_groups(" ))"
print(separate_paren_groups("  function))
print(separate_paren_groups('(' function' )))
print(separate_paren_groups('( )'))
print(separate_paren_groups('()   '))
```