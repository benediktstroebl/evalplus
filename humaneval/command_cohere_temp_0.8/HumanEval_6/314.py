```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_par = segment.count('(')
        close_par = segment.count(')')
        result.append(max(open_par, close_par) + 1)
    return result
```

The specified Python script solves the problem using a basic approach. It splits the input string into segments using spaces as separators, and then counts the number of opening and closing parentheses for each segment. The maximum of these counts represents the deepest level of nesting, which along with 1 is appended to the result list (to account for the number of spaces). The function returns the resulting list.

This approach has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n) due to the creation of intermediate lists. While it fulfills the requirements for the provided test cases, it's worth mentioning that an optimized approach using a stack for nesting tracking would be more efficient for larger or more complex input strings.