```python
def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Create a dictionary to store the mapping of opening and closing brackets
    bracket_map = {">": "<", "<": ">"}
    
    # Create a stack to store the opening brackets
    opening_brackets = []
    
    # Iterate over each character in the input string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            opening_brackets.append(bracket)
        # If the character is a closing bracket, check if the stack is empty or the top of the stack does not match
        elif bracket == ">":
            if not opening_brackets or opening_brackets.pop()!= bracket_map[bracket]:
                return False
    
    # After iterating over the entire string, return False if there are any remaining opening brackets in the stack
    return not opening_brackets


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```