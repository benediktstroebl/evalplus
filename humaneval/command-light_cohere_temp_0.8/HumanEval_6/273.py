```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    results = []
    for group in parent_string.group():
        pattern = r'\([^\)]+\)$'
    while group:
        match = re.match(pattern, group)
        if match:
            stack.append(match.match.match.stack.match
       start aanga result with a final element, otherwise, and will be added to the results list. Otherwise, it will be added to the stack for the next iteration.
    match.
)
    return stack
stack.results
```