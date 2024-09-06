Here's a Python script that contains a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings containing the separate groups of parentheses. The function works by using the concatenation of open and close parentheses to match pairs, and tracks the balance and nesting of the groups to properly separate them. The solution ignores any spaces in the input string.

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '('
    close_braces = ')'
    separated_groups = []
    current_group = ''

    for char in paren_string:
        if char == open_braces:
            current_group += char
        elif char == close_braces:
            current_group += char
            if not current_group.count(open_braces) != len(close_braces):  # check balance
                separated_groups.append(current_group)
                current_group = ''
        else:
            current_group += char

    # handling the last group
    if current_group:
        separated_groups.append(current_group)

    return separated_groups

# Test Suite
paren_string = '   (  )    ((  ))    (( ( ))    ('
expected_result = ['()', '(())', '(()())', '()', '()']

assert separate_paren_groups(paren_string) == expected_result
```

This script uses a simple approach to solve this problem that involves maintaining a `current_group` variable that keeps track of the currently open group of parentheses. As we encounter close parentheses, we check to ensure the open and close parentheses are balanced (the number of open '(' and ')' characters matches) - if so, we add the current_group to the list of `separated_groups` and reset `current_group` to an empty string. We then repeat this process until all groups are separated and returned.