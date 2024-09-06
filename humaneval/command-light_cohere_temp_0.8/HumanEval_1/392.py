```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    return [brace.join(r) for brace, r in input_string.join() if brace != ' ')
```

This function takes an input string containing multiple groups of parentheses and returns a list of separated strings, where each separated string corresponds to a balanced group of parentheses. The function uses the join() method with a regex pattern (r) to match and combine each balanced group of parentheses into a single string.