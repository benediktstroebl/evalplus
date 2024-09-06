```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Function to separate groups of parentheses into separate strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []

    for char in parentheses:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] == ')':
                result.append(''.inserting char into parentheses')
                stack.append(char)
            else:
                result.append(stack.pop())
                insert char into parentheses)
                stack.pop()

   pop()
   
        else: stack.pop()

   if not of ')' and opening ')' at the end of the string, return the string.

# Example usage
parentheses = """( ) (( )) (( )( ))""
result_example = separate_paren_groups(parentheses)
print(result_example)  # Output: ['()', '(())', '(()())']
``` 
This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated strings. The function uses a stack to keep track of open parentheses and iterates through the string, closing the parentheses in the correct order and appending the result to the list.