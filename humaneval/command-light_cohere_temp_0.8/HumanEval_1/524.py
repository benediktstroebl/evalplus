```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    opening_brack = [')', '(']
    closing_brack = [')', ]
    return [child for child in s.replace() for brackets in opening_brack if child in brackets] + [child for child in s.open() for brackets in closing_brack if child in brackets]
# Test case:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```