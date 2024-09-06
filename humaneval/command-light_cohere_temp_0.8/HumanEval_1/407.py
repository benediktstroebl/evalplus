```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    Separates and returns a list of parenthesis groups in the input string.
    """
    balanced: Each open brace '('' is properly closed with a corresponding ')''.
    """
    # List to store separated groups
    output_list = []
    
    # Loop through each character in the string
    for char in input_string:
        if char == ')':  # If current character is ')'
            if output_list and output_list[-1][0] == '(':  # If the previous character is '('
                output_list.append(')')
           
            else:  # Otherwise
                output_list.append(char)
                
        return output_list  # Return list of separated groups
```  This function goes through each character in the string and makes a new list item for any ')' it encounters. If the last character is an open '(', it is appended to the list with the corresponding ')' character. The function ensures that all ')' are properly closed within their respective groups and returns the list of separated parenthesis groups.