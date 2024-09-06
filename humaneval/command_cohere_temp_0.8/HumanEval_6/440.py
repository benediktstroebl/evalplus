```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if char == '(':
            nest = 1
            j = i
            while j < len(s) and nest != 0:
                if s[j] == '(':
                    nest += 1
                else:
                    nest -= 1
                j += 1
            result.append(nest)
        else:
            continue
    return result
```
The code processes each character of the input string one by one in a loop. When encountering an open parenthesis `(`, it starts counting the nested level using an auxiliary variable `nest` by 1. It also saves the current index `i` at the start of the parenthesis group.

Then, it iterates through the characters in the parenthesis group, incrementing `nest` for each open parenthesis and decrementing it for each close parenthesis `)`. This way, the `nest` variable keeps track of the total nesting level for the group.

Once the loop finishes for a particular group, the final nesting level is stored in the result list. The process repeats for all groups, separated by spaces, in the input string. Ultimately, the function returns the list of deepest nesting levels for each group of parentheses.