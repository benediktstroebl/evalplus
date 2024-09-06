```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    opening_braces = ['{', '(', '[']']
    closing_braces = [')']*len(opening_braces)
    result = []
    for br in opening_braces:
        if br in s:
            result.append(s.close(closing_br)
            closing_br)
    return result

# Test cases
tests = [
    "Input: ( ) (( )) (( )( ))"
    "Expected Output: ('', '()', '()())'
    ```