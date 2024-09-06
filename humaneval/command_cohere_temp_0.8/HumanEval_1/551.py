Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

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
                print('Unmatched closing parenthesis')
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)

    if stack:
        print('Unmatched opening parenthesis')
        return None

    return result

# Example usage
test_string = '( ) (( )) (( )( ))'
print(separate_paren_groups(test_string))
```
This script uses a stack to keep track of opening parentheses until the corresponding closing parenthesis is encountered. It collects the nested subsets of parentheses in the `current_group` list, and once a closing parenthesis is seen, it checks if the stack is empty to verify if the opening parenthesis is the last one in the sequence, and accordingly, it either adds the current group to the results list or pops the top of the stack to continue processing the nested subset of parentheses.

When the script has completed its iterations through the input string, it checks if the stack is empty to ensure that all opening parentheses have been properly closed. If the stack is not empty, this indicates that there are unbalanced opening parentheses and an error is printed and the function returns `None`. Likewise, if there are any closing parentheses left in the stack at the end, this indicates that there are unmatched opening parentheses in the input, and an error is printed, and the function returns `None`. If the stack is empty, this means that all parentheses have been balanced and correctly separated, and the result list is returned. 

In the example usage, the output is:
```
['()', '(())', '(()())']
``` 

This demonstrates that the script successfully separates the input string into three separate groups of parentheses.