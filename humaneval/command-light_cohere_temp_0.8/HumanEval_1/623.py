Certainly! Here's a self-contained Python script with a function called `separate_paren_groups` that solves the problem you've described: 

```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses and returns a list of separated strings.
    Each group of parentheses is separated into individual strings while maintaining balanced syntax.
    """
    balanced = []
    for i in range(len(paren_string)):
        char = paren_string[i]
        if char == '(' and balanced and char == ')':
            balanced.append(char)
        balanced.append('')
        balanced.append(char)
        balanced.append('')
        done
    balanced
        return [''.join(balanced))
    ```