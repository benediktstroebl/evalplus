```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string with parenthesis groups and returns a list of separated strings.
    >>> return separate_paren_groups('(( )) (( )( ))')
    ['()', '( )', '(() )']
    """
    return [w for w in s.remove('()') if w.isalpha()]
 separate_paren_groups(')  )  )  )  )  )  )  )
```
This code defines a function called `separate_paren_groups` which takes a string s as input and returns a list of strings, each coming from a separate parenthesis group. The code uses the string's remove all parenthesis and non-alpha characters, and then creates a list from the words in the string.