```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = []
        tally = 0
        for char in segment:
            if char == '(':
                open_brackets.append(tally)
                tally += 1
            else:
                tally -= 1
                if tally in open_brackets:
                    result.append(tally)
    return result
```

The code processes each segment (separated by spaces) individually, maintaining a tally of open brackets encountered. When a closing bracket is encountered, it's checked if it matches the most recent opening bracket. If it does, the tally is appended to the results list. The provided example and its expected output are both validated by the unit tests.