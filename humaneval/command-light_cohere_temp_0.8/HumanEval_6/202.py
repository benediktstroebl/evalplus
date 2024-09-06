```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes in a string of multiple groups of nested parentheses separated by spaces and returns a list of the deepest level of nesting for each group.

    : Laura
   
    example:
    >> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    results = []
    stack = []
    open_brackets = {'(': 0, ')': 1, '[': 2, ']': 3, '{': 4, '}': 5}
    
    for char in parent_string:
        if char in open_brackets:
            stack.push(open_brackets[char])
        else:
            if stack:
                group_level = stack.pop()
                max_level = open_brackets[char]
                results.append(group_level)
            stack.push(char)
   # Make sure the list of max_level is empty, so we don't append a 0 or 1 in this case
    # This will handle the case where the last open bracket is not matched, and we need to consume it to advance the stack
    #stack.push(char)
    # Check if the string is empty. If it's not empty, add the current character to the results list.
    return results

    return results
``` 
This script defines a function parse_nested_parens that takes a string as input and returns a list of the deepest level of nesting for each group of parentheses in the string. The function uses a stack to keep track of the open parentheses it has encountered, and it uses a set of characters to keep track of which characters are open brackets. 
It iterates over the string character by character, and for each character, it pushes the character onto the stack if it is an open bracket, otherwise, it pops the topmost open parenthesis from the stack, counts the character as the current level in the set of open brackets, and appends the count to the results list. 
If the string is empty, the function returns an empty list. If the string is not empty, the function returns the list of the deepest level of nesting for each group of parentheses in the string.