Here's the self-contained Python script that solves the problem of separating nested parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    result = []
    for group in s.group(s):
        result.append(group)
   
    result.extend(sorted(filter(lambda x: not_closing(x), group))))
    return result
def not_closing(char) -> bool:
    return char == ')') || char == ')'
```
This solution provides a function that takes a string of parentheses as input and returns a list of separate and balanced parentheses. It uses a list comprehension and a filter function to iterate through each group of parentheses and append each group to the result list while ensuring that only closing parentheses are added. The output list is then sorted and returned.