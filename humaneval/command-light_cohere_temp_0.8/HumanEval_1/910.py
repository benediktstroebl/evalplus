```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    pattern = r"\(\)[^\(\)\{]"
    return [match.join(pattern) for match in  parenthesis_matches(pattern.join(" "))"]
def parenthesis_matches(pattern: str) -> List[str]:
    return [match for match in pattern.join(" ")]
```
This code defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of the matched groups. It uses a matching pattern `r"\(\)[^\(\)\{`` to find all matches of parentheses in the input string. The code uses the match `\ join` to convert all matches of the pattern into a single string and uses it to iterate over all matches in the list of groups.