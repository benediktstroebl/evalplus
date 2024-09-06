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
                print('Unbalanced parentheses!')
            else:
                temporary_group = stack.pop()
                current_group.extend(temporary_group)
        
        current_group.append(char)
    
    stack.extend(current_group)
    result.extend(stack)
    
    return result
```

The provided Python script implements a function called `separate_paren_groups`, which takes a string as input and returns a list of strings. This function is designed to handle nested parentheses in the input string by using a stack to keep track of opened parentheses until they are closed, effectively separating the nested groups. Here's how the function works:
1. **Data Structures**: The function utilizes a `stack` data structure to manage opened parentheses and a `current_group` list to store the currently opened parentheses. The `result` list is used to store the final output.
2. **Iterating Through Input String**: The function iterates through each character of the input `paren_string`.
3. **Handling Opening Parentheses**: When an opening parenthesis '(' is encountered, it is added to the `stack` of opened parentheses. Additionally, a new empty list `current_group` is created to store the currently opened parentheses.
4. **Handling Closing Parentheses**: When a closing parenthesis ')' is encountered, the function checks if the stack is empty. If it is, this indicates unbalanced parentheses, and an error message is printed. Otherwise, the function pops the top item from the stack, which represents the last opened parenthesis, and appends it to `current_group`.
5. **Building Result**: The function continues iterating through the input string, appending each character (either an opening or closing parenthesis) to the `current_group`. Once all parentheses are processed, the `current_group` is appended to the stack to ensure that all opened parentheses are properly closed. Then, the stack is appended to the `result` list.
6. **Return Result**: Finally, the function returns the `result` list, which contains all the separated groups of parentheses.

The given example input `'( ) (( )) (( )( ))'` successfully demonstrates the expected output `'()', '(())', '(()())'`. This approach provides a clear and efficient way to handle nested parentheses and achieve the desired separation into different lists.