```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in reversed(list( BracketCounter(s)) ):
        result.append(bracket_level)
    return result

class BracketCounter:
    def __init__(self, text: str):
        self.text = text
        self.level = 0
        self.brackets = {')': ('(', '['), '}': '(', '['}

    def __iter__(self):
        return self

    def __next__(self):
        if not self.text:
            raise StopIteration
        char = self.text.pop()
        self.level += 1 if char in self.brackets['}'] else -1
        return self.level

```
The code uses a counter of brackets and a stack to calculate the deepest level of nesting of parentheses in each of the groups.