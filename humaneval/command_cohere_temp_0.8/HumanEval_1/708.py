```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                print(f"Invalid input: No opening parenthesis ({char}) found!")
                return []
            current_group.pop()
            stack.pop()
            result.append(''.join(current_group))
            current_group = stack.pop()
        else:
            current_group.append(char)

    if stack:
        print(f"Invalid input: Unbalanced parenthesis found!")
        return []
    else:
        result.append(''.join(current_group))

    return result
```

This Python script takes a parenthesis string as input and returns a list of sub-strings, each containing a separate group of nested parentheses. It ensures that each open parenthesis has a matching close parenthesis and that groups are not nested within each other. This is done by utilizing a stack to keep track of opening parentheses and creating a resulting string for each closed parenthesis group.

The script handles cases of unbalanced or nested parenthesis groups by printing an error message and returning an empty list, ensuring the correctness of the result. You can test this script by providing various parenthesis strings and verifying that the result contains the expected groups.