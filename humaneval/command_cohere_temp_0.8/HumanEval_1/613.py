```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                return ['Invalid input! No opening parentheses to match this closing parenthesis.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        return ['Invalid input! Missing closing parenthesis']
    else:
        result.append(''.join(current_group))
        return result
```

This Python script takes a string as input and returns a list of strings. Each string in the list represents a separate
group of nested parentheses, and each open parenthesis has a matching closed parenthesis. The script guarantees
that each group is balanced and not nested within each other. 

The program solves this problem using a stack, a common data structure to solve recursive problems like this one. 

To understand how the program works, let's break it down step by step:
1. First, we import the `List` module from the typing library. This is needed because we want to return a list of
strings at the end.
2. Next, we define our function `separate_paren_groups(paren_string)` that takes in a string of parentheses
and returns a list of strings, each representing a separate group of parentheses.
3. Inside the function, we initialize two important variables: `stack` and `current_group`. `stack` is a list that
will hold the nested strings of parentheses as we parse the input string. `current_group` is initially an empty
string but will later hold the current group of parentheses being analyzed.
4. We also initialize an empty list called `result` that will later hold our final answer, which is a list of
separated parentheses groups.
5. We iterate over the input string character by character using a for loop.
6. If the current character is an open parenthesis `(`, we do two things:
    - We push (add to the top of) the `current_group` to the `stack`. This saves the current group of
    parentheses so that we can come back to it after finding its matching closing parenthesis.
    - We initialize a new empty string `current_group` to start building the new group of parentheses.
7. If the current character is a closing parenthesis `)`, we check if the `stack` is empty. If it's empty, this
means we have an unmatched closing parenthesis, and we return an error message indicating an invalid input.
So we return the special string `['Invalid input! No opening parentheses to match this closing parenthesis.']`.
8. If the stack is not empty, we pop the top of the stack into `current_group`. This recovers the previously
saved group of parentheses that has a matching opening parenthesis. Now the `current_group` variable holds
a string of parentheses that is properly matched and nested within the group represented by the top of the
stack.
9. If the current character is neither an opening nor a closing parenthesis, it must be something else, like
an inner punctuation mark or a space. In this case, we simply append it to the `current_group`. This allows us
to ignore spaces and other inner punctuation marks when separating the groups.
10. After the for loop, we check if the stack is empty. If it's not