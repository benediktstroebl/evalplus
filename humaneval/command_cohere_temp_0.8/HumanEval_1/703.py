Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings that represent the individual groups of parentheses:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '([{'
    close_braces = ')]}'
    paren_groups = []
    current_group = ''

    for char in paren_string:
        if char in open_braces:
            current_group += char
        elif char in close_braces:
            if not current_group:
                # Ignore unnecessary closing braces
                continue
            else:
                paren_groups.append(current_group)
                current_group = ''
        else:
            current_group += char

    if current_group:
        paren_groups.append(current_group)

    return paren_groups

# Sample input and expected output
paren_string = '( ) (( )) (( )( ))'
expected_output = ['()', '(())', '(()())']

print(f"Input: {paren_string}")
print(f"Output: {separate_paren_groups(paren_string)}")
print(f"Expected Output: {expected_output}")
```
This script defines the `separate_paren_groups` function and uses a loop to iterate through the input string, keeping track of opened parentheses and properly closing them before adding the group to the output list. The script also includes a sample input and expected output to demonstrate the function's behavior. The output shows the function's behavior when provided with different parentheses combinations.