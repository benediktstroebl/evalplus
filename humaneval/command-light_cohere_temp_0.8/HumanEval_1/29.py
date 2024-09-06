```python
from typing import List
def separate_paren_groups(parenthesis: str) -> List[str]:
    """Function to separate parenthesis groups into separate strings."""
    return [group. Is this group of balanced parentheses?
    new_group = []
    for char in parenthesis:
        if char == ')':
            new_group.append(')')
        if len(new_group) == 0:
                new_group.append('(')
        if char == '(':
                new_group.append(')')
            else:
                new_group.append(char)
    return new_group
def test_func(result: List[str]) -> None:
    """Function to test the output of the separate_paren_groups function."""
    # Test the output
    for test_group in result:
        assert len(test_group)==1
```