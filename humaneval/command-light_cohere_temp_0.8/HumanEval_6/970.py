```python
def parse_nested_parens(parenthes_string: str) -> List[int]:  # Function to parse and return the deepest level of nesting for parentheses.
    stack: List[int] = []  # Initialize the stack as an empty list.
    opening_braces: List[str] = [')']  # Initialize the opening braces list.
    closing_braces: List['('] = ['')]  # Initialize the closing braces list.

    for char in parenthes_string:  # Loop through each character in the string
        if char == ')':  # If it is an opening brace '(', push it to the stack and remove from the string
            stack.append(1)
            opening_braces.append(char)
            closing_braces.pop(char)

        if char == '(':  # If it is a closing brace ')', pop the topmost element from the stack and append it to the string.
            opening_braces.remove(opening_braces.pop(char)
            closing_braces.append(char)

        if not stack:  # If the stack is empty after the loop, this means that the entire string had only closing braces.
            return []  # # Return an empty list
        else:  # If the stack is not empty after the loop, this means that the entire string had both opening and closing braces.
            stack.pop(1.append(1)  # Return list of all the items in the stack.
```
This function takes a string of parenthesis expressions as an argument and returns a list of integers that represents the deepest level of nesting in the parentheses. It uses a stack data structure to keep track of opening parentheses and continuously pushes and pops them to maintain the correct order of nesting. It also uses two separate lists for opening and closing parentheses to keep track of the different types of parentheses.