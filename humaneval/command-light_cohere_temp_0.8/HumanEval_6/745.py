Here is a Python script that contains a self-contained function that solves the problem of parsing nested parentheses:
```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    # Create a list to store the nested levels
    nested_levels = [] 

    # Initialize the counter of nested levels with 1
    level = 1

    # Iterate through each character in the string
    for char in parenthes_string:
        # If the character is a left parenthesis
        if char == '(':
            # If the current level is the deepest level, add 1 to the counter
            level += 1

        # If the character is not a left parenthesis and it's not the last character in the string
        elif char != ')':
            # Append the current character to the list for the current level
            nested_levels.append(char)

        # If the character is a right parenthesis and the current level is the deepest level
        else:
            # Decrease the counter by 1
            level -= 1
            # If the counter becomes 0, this means that we reached the outermost level of nesting, so we are done
            if level == 0:
                break

    # Reverse the order of the nested levels list
    nested_levels.reverse()

   
    final nested levels
    ``` [1, 3, 2, 4] 
This script defines a function, `parse_nested_parens`, which takes a string as input and returns a list of nested levels. It uses a negative indexing to track the deepest level of nesting, and uses a counter to keep track of the number of groups of parentheses. The function works by iterating through each character in the string, adding the character to the appropriate nested levels list if it is a left parenthesis. If the character is a right parenthesis, it decreases the counter by 1 and breaks out of the loop. If the counter becomes 0, it means that the string has finished, so the function returns the nested levels list.