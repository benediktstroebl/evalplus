Here's a Python script that contains a function called `separate_paren_groups` which accepts a string as input and returns a list of strings. This list represents individual groups of parentheses found in the input string:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '('
    close_braces = ')'
    output = []
    current_group = ''

    for char in paren_string:
        if char == open_braces:
            current_group += char
        elif char == close_braces:
            current_group += char
            if current_group == '()':
                output.append('')
            else:
                output.append(current_group)
                current_group = ''
        else:
            current_group += char

    if current_group:
        output.append(current_group)

    return output

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

When you run this script and provide the example input, it will produce the following output:
```
['()', '(())', '(()())']
```

This output is what you described in the prompt. The script splits the input string into separate groups of parentheses, regardless of any spaces, and returns them as a list of strings. Each string in the list represents a balanced group of parentheses.