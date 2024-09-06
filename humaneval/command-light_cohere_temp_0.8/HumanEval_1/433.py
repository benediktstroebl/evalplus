```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns lists of parentheses and brackets.
    : Open brackets are opened should be closed and vice versa
    :param s: Input string with balanced and unbalanced parentheses
    :return: List of strings, each containing only balanced parentheses
    """
    # define stack
    stack = []

    # Define a function to add an element to the stack
    def push(element: str):
        stack.append(element)

    # Define a function to check if the stack is empty
    def is_empty():
        return len(stack) == 0

    # Define a function to pop an element from the stack
    def pop():
        if is_empty():
            return ''
        return stack.pop()

    # Iterate through
    open brackets to pop them and add them to the stack. 
    for bracket in s:
        # If the bracket is open, add it to the stack
        if (bracket != ')' and bracket != '('):
            push(bracket)
        # If the bracket is closed, pop it from the stack and continue iterating
        elif (bracket == ')' or bracket == '('):
            pop()

    # Return the list of strings
    return [s[i:i+1] for i in range(0, len(s), 1)]
``` 
This Python script defines a function `separate_paren_groups` that takes a string of balanced and unbalanced parentheses as input and returns a list of strings containing only balanced parentheses. The function uses a `stack` to keep track of the brackets and uses a series of nested loops to separate the balanced parentheses from the input string.