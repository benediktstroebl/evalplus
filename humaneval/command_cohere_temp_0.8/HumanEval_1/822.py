Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings of separated parentheses groups.

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                return []
            top_group = stack.pop()
            if not top_group:
                result.append(current_group)
            else:
                current_group = top_group + current_group
        else:
            current_group += char
            
    return result

# Sample input and expected output
paren_string = '( ) (( )) (( )( ))'
expected_result = ['()', '(())', '(()())']

result = separate_paren_groups(paren_string)
print(f"Input: {paren_string}")
print(f"Output: {result}")
print(f"Expected Output: {expected_result}")

```
This code defines a function that takes a string as its input and returns a list of strings containing nested parentheses. 

The program works as follows:
1. It sets up a blank list called `stack` to hold our separate groups, and initializes an empty string called `current_group` to capture the currently open braces. 
2. We iterate through each character in the input string. If it's an open parentheses '(', we do the following:
    - append the current group to the stack. Note that if the current group is empty, it means we just hit an open brace '(' without a corresponding closing parenthesis ')', and we'll simply ignore it. This ensures that our groups are balanced.
    - Initialize the `current_group` to an empty string to prepare to capture the next brace group.
3. If the current character is a closing parenthesis ')', we do the following:
    - Append the character to the `current_group` buffer. This ensures that we maintain the balance of closing and opening parentheses.
    - Check if the stack is empty. If it is, it means we've reached the end of a balanced brace group. In this case, we add the current_group to the result list (if it's non-empty) and continue the loop.
    - Otherwise, we pop a group from the stack. This is because each opening parenthesis '(' we encounter must match a corresponding closing parenthesis ')' _and_ the group must not be nested within another group. In other words, it's anchoring itself to the top of the stack, which contains the closest matching parentheses to the current index. If the group we popped is empty, it means this is the start of a new group, so we append the current_group to the top of the stack (which is the most recent group we popped), and continue processing. If the group we popped is not empty, that means we have reached the end of a nested group, so we replace the current_group with the popped group + the current_group, effectively joining the nested groups. 
4. For all other characters (either space ' ' or any other symbol), we append them to the current_group.
5. Once we've iterated through the entire input string, we return the result list, which contains all the separated nested parentheses groups.

The sample input and expected output demonstrate how the program works and shows