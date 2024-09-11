```markdown
### Correct Bracketing Function

#### Problem Description

A string of parentheses is said to be correctly bracketed if every opening parenthesis has a corresponding closing parenthesis. This function checks if a given string of parentheses is correctly bracketed.

#### Code

```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack
    
    for bracket in brackets:
        # If the bracket is an opening parenthesis, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the bracket is a closing parenthesis, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, there's no corresponding opening parenthesis, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening parenthesis from the stack
            else:
                stack.pop()
    
    # After iterating over the string, if the stack is empty, it means every opening parenthesis has a corresponding closing parenthesis
    # So return True
    # If the stack is not empty, it means there are unmatched opening parentheses, so return False
    return not stack

#### Test Cases

print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

#### Explanation

This function uses a stack to keep track of the opening parentheses. When it encounters an opening parenthesis, it pushes it onto the stack. When it encounters a closing parenthesis, it checks if the stack is empty. If the stack is empty, it means there's no corresponding opening parenthesis, so it returns False. If the stack is not empty, it pops the opening parenthesis from the stack. After iterating over the string, if the stack is empty, it means every opening parenthesis has a corresponding closing parenthesis, so it returns True. If the stack is not empty, it means there are unmatched opening parentheses, so it returns False.