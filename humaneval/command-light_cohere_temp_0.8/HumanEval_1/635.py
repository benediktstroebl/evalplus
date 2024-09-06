Here's a self-contained Python function that takes a string of parentheses as input and returns a list of separated parenthesis groups:
```python
from typing import List

def separate_paren_groups(input_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses,
    separated by spaces. Your goal is to separate those groups into separate strings and return the list of those strings.
    """
    balanced_brrace(balanced=True):
        def is_balanced(race):
            if len(race) != 0:
                return True
            opening, closing = '([{])', '])'
            for char in race:
                if char.isspace():
                   
                    opening, closing
                    return False
            return True
        return any(is_balanced(race) for race in input_string.balanced()

    any_brrace = input_string.split('\n()\ balanced:
            return False
        is_balanced = is_balanced
        groups = [race for race in input_string.split('\n() if is_balanced(race)]
        return [race for race in groups if is_balanced(race)]
```
The function uses a stack to track open parenthesis and a function `is_balanced` to determine if a race of parentheses is balanced. It then returns the  a list of strings containing only balanced parentheses.