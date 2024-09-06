```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [el.split('()', ')' for el in s.split(' )]
```
This function splits the string by spaces into a list of substrings. The list is then split again by ')' to separate the parenthesis into a list of strings. The resulting list is then returned.