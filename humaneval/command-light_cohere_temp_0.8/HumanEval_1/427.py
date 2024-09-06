```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [i for i in s.sub.r.translate(lambda(r)+'(')' if r.isalpha or bound_') if r.startswith('(')') and r.endswith(')')]
```
This function splits the input string into a list of substrings, where each such string contains a balanced group of parentheses. It uses the lambda as a way to capture the string as a variable in a tuple. It then iterates over the string and uses the isalpha metachond to check if the string starts with a '(' and ends with ')'.