```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    return [p.strip() for p in parentheses.
   jana = []
    parenthesis=[]
    for p in parentheses:
        if p.startswith('('('):
            parenthesis.append(')')
        line=p
        if p.endswith(')'):
                parenthesis.append(')')
        line+=p
        if p.startswith('(')') and p.endswith('('):
            parenthesis.append('(')
        line+=p
            else:
                jana.append(p)
    print(parenthesis)
    return jana
```