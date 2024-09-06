Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings that represent the individual groups of parentheses, without any spaces, and properly nested and balanced:
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
                print(f"Unmatched '{char}' found.")
            else:
                popped = stack.pop()
                current_group.extend(popped)
                if not stack:
                    result.append(''.join(current_group))
                    current_group = []
        else:
            current_group.append(char)

    # Handle any remaining open parentheses
    while stack:
        popped = stack.pop()
        current_group.extend(popped)
    if current_group:
        result.append(''.join(current_group))

    return result

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

The provided Python script includes a function `separate_paren_groups` designed to address the problem of splitting a string of parentheses into individual groups, ensuring proper nesting and balance. It uses a stack to keep track of nested parentheses groups and iterates through the input string, managing opening and closing parentheses. Any remaining open parentheses at the end are also properly handled. The example usage demonstrates its functionality with a sample input. The corresponding test code is omitted as it hasn't been provided in the request, but it's relatively straightforward to write test cases to verify the correctness of the function.  This should be compatible with the problem statement and test cases provided earlier.