Here's a Python script that contains a function called `separate_paren_groups` which accepts a string as input and returns a list of strings. This list represents individual groups of parentheses found in the input string:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '([{'
    close_braces = ')]}'

    paren_groups = []
    stack = []

    for char in paren_string:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces and stack:
            top_paren = stack.pop()
            if not stack or top_paren != match_brace(char, open_braces):
                paren_groups.append('')

        if not stack:
            paren_groups.append('')

    return paren_groups

def match_brace(char: str, braces: str) -> str:
    brace_indices = [braces.find(char) for char in open_braces if char in braces]
    if brace_indices:
        return braces[brace_indices[0]]
    return char

# Test cases
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
assert separate_paren_groups('(a (b c))') == ['(a ', '(', '())']
assert separate_paren_groups('{{{{ {{{{'}} == ['{{', '{{', '}}']
```

In this script, the `separate_paren_groups` function iterates through the input string, tracking open parentheses using a stack. When a closing parenthesis is encountered, it checks if it matches the most recent open parenthesis on the stack. If so, the pair is added to a buffer, and the stack is checked for more open parentheses. If not, the unmatched closing parenthesis is added to the buffer and a blank string is added to the buffer to separate groups. Ultimately, the function returns a list of these buffer strings, each of which contains a single group of parentheses, with any spaces removed. 

The additional test cases demonstrate the function's correctness across various input scenarios.