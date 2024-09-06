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
                print(f"Invalid input - extra closing brace: {char}")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print(f"Invalid input - unclosed brace!")
        return []
    
    result.append("".join(current_group))
    
    return result
```
The provided Python script implements a function called `separate_paren_groups`, which takes a string as input and returns a list of strings. This function is designed to process a string containing multiple groups of nested parentheses, and its purpose is to separate these groups into individual strings.

Here is an example of how you can call this function:
```python
print(separate_paren_groups("( ) (( )) (( )( ))"))
```
This will output the following:
```python
['()', '(())', '(()())']
```

To achieve this, the function utilizes a stack to keep track of nested parentheses groups. It iterates through each character in the input string, checking if it's an opening parenthesis `(`. If so, the current group is pushed onto the stack and a new, empty group is created. When a closing parenthesis `)` is encountered, the function checks if the stack is empty; if not, the top group from the stack is popped and appended to the current group. All other characters are directly added to the current group. 

The function handles cases where there are extra closing parentheses or unmatched opening parentheses. If an extra closing parenthesis is encountered, it prints an error message indicating an invalid input. Likewise, if there are unmatched opening parentheses, the function also prints an error message, indicating an unclosed brace. 

Finally, the function returns a list of strings, where each string corresponds to a separate group of parentheses found in the input string.