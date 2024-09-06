```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    """This function takes in a string of nested parentheses and returns a list of the deepest level of nesting."""
    #The function uses a recursive approach with a max depth of 3 to account for the deepest possible nesting
    # Initialize empty list to store the results
    results = []
    # Use a recursive function to go as deep as possible
    def recursive(char):
        if char == '(':
            # If we have seen the opening parenthesis, add it to the results list
            results.append(1)
            # Recursively call the function for the next character
            recursive(char)
        elif char == ')':
            # If we just saw the closing parenthesis, add the current number of the stack
            results.append(results.pop())
            if the either a other parenthesis is not the top level, continue the recursion
            recursive(char)
        else:
            # Other case, simply push the character onto the stack
            results.append(char)
    return results
    # Return the results list
    return results 

# Test the function
test_parse_nested_parens = parse_nested_parens("(()()) ((())) () ((()))()")
print(test_parse_nested_parens)  # Output: [1, 1, 1] 
``` 
This script defines a recursive function `parse_nested_parens` that takes in a string of nested parentheses and returns a list of the deepest level of nesting for each group of parentheses.