```python
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack = []
    output = []

    for char in parenthes_str:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                output.append(char)
            else:
                stack.append(char)
                if len(stack) == 3:
                    output.append(int(')', len(stack) - 3))
                    stack = stack[0:-1]
                else:
                    stack.append(char)

    return output
``` 
This function takes a string of parenthesis characters as input and returns a list of the deepest level of nesting of parentheses. 

The function uses a stack data structure to keep track of the last character seen. 

This way, it can output the deepest level of nesting without having to consider all the characters before it. 

The function works by iterating through the string, and when it encounters an open parenthesis, it appends it to the stack. When it encounters a closed parenthesis, it adds it to the output and then pops all the characters from the stack to continue iterating. 
When it encounters another open parenthesis, it checks if the stack is empty, and if it is, it appends the character to the output. 
If the stack is not empty, it appends the character to the stack and checks if the stack is now three characters long. If it is, it appends the integer ')' to the output and then pushes the topmost element from the stack back onto it.