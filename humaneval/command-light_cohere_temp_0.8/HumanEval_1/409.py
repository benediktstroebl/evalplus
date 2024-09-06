```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Return a separated groups as a list of those strings.
    """
    for group in s.group :=braces(s):
        if ')' in group:
            yield group[::-1]
        else:
            yield group

# Example test
test_string = r"(()(\)\s*(_)\))"
result = separate_paren_groups(test_string)
print(result)
```