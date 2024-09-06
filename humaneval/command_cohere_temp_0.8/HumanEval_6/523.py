```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        nest = 0
        for c in chunk:
            if c == '(':
                nest += 1
            else:
                nest -= 1
        result.append(nest)
    return result
```
The `parse_nested_parens` function takes a string as input and splits it into chunks based on spaces. It maintains a `nest` variable to keep track of the current nesting level for each chunk. If a `(`) is encountered, the `nest` value is increased, and for every `)` encountered, the `nest` value is decreased. The final nesting level for each chunk is appended to a result list, which is returned after processing all chunks. 

This solution does not require any additional libraries, such as `re`, to be installed. While such libraries can make certain tasks easier, they are not necessary for this problem and would make the solution less self-contained, as mentioned in the prompt.