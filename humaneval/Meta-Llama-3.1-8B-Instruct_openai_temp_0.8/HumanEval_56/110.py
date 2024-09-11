```python
def correct_bracketing(brackets: str):
    """ 
    This function checks if a given string of "<" and ">" brackets is correctly bracketed.
    A string is correctly bracketed if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">" brackets.

    Returns:
        bool: True if the string is correctly bracketed, False otherwise.
    """
    
    # Initialize a counter to keep track of opening brackets
    opening_brackets = 0
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "<":
            opening_brackets += 1
        # If the character is a closing bracket, decrement the counter
        elif bracket == ">":
            opening_brackets -= 1
            
            # If the counter becomes negative, there are more closing brackets than opening brackets
            # So, the string is not correctly bracketed
            if opening_brackets < 0:
                return False
                
    # If there are any remaining opening brackets, the string is not correctly bracketed
    # This is because there are no corresponding closing brackets
    if opening_brackets!= 0:
        return False
    
    # If the function has not returned False by now, the string is correctly bracketed
    return True

# Test cases
print(correct_bracketing("<"))  # Should print: False
print(correct_bracketing("<>"))  # Should print: True
print(correct_bracketing("<<><>>"))  # Should print: True
print(correct_bracketing("><<>"))  # Should print: False
```
This script defines a function `correct_bracketing` that checks if a given string of "<" and ">" brackets is correctly bracketed. It uses a counter to keep track of the number of opening brackets. If the number of closing brackets is greater than the number of opening brackets at any point, or if there are any remaining opening brackets at the end, the function returns False. Otherwise, it returns True. The script also includes test cases to demonstrate the function's behavior.