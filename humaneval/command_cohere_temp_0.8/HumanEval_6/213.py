```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(len, group.split())))) for group in s.split(' ')]
```

The logic of the solution is to treat each group from the input string s as a list of strings where each string is a direct substring of the group separated by spaces, sort these substrings by their lengths in descending order and accumulate them into a single string whilst keeping track of the nesting levels with the help of modulo operation (i.e. len('((()))') -> 3, len('(()())') -> 2, etc.) and take the maximum nesting level for each group. Finally, the function returns a list where each element corresponds to the deepest level of nesting of parentheses for each group.

This code assumes that the input string follows the given problem statement and is structured correctly. You can adjust the code to handle any invalid inputs according to your needs.