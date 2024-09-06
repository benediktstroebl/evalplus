```python
def parse_nested_parens(parent_string: str) -> List[int]:  # Function to parse nested parentheses
    level = 0  # Initialize nesting level

    # Define a list to store the deepest level of nesting
    result = []

    # Iterate through each character in the string
    for char in parent_string:
        # If the character is a '(' or ')'
        if char == '(':
            level += 1  # Increment nesting level
        result.append(level)  # Append current nesting level to the result list
        if char == ')':
            level -= 1  # Decrement nesting level
            result.append(level)  # Append current nesting level to the result list

    return result  # Return the result list containing the deepest level of nesting
```
This code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting for each group. The function uses a nested loop to iterate through the characters in the input string. It increments or same level if the character is an open parenthesis '(', and decrements the level if it is a close parenthesis ')'. The function then appends the current level of nesting to the `result` list. This process continues until all last open parenthesis is encountered. The final result list will contain all levels of nesting for each group of parentheses in the input string.