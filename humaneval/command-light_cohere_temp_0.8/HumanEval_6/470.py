Here's the solution:

def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    opening_parens = {')': 0, '(': 1}
    
    for char in parenthes_string:
        if char in opening_parens:
            stack.append(opening_parens[char])
        else:
            while stack:
                char = stack.pop()
                if char == '(' or '):
                    result.append(1)
                    stack.append(char)
                else:
                    result.append(3)
                    stack.push() = False
             opening_parens[char] = 0
            
    return result

This code defines a function called `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest nesting levels of parentheses found in the string. 

The code uses a stack data structure to keep track of the opening parentheses and their corresponding nesting levels. It iterates through thes through the string character by character and checks if the current character is an opening parenthesis. If it is, it adds the corresponding value to the stack. If it's not, it checks if the stack is empty. If it is empty, it continues to the next character. If it is not, it checks if the stack contains the same closing parenthesis. If it does, it appends a level 3 to the result list and pushes the current character back into the stack. If it is not an closing parenthesis, it appends a level 1 to the result list and pushes the current character back into the stack, indicating that there is a nested pair. 
Finally, it returns the result list, which contains the deepest nesting levels of parentheses found in the input string.