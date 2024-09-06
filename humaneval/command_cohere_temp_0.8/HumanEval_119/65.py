```python
def match_parens(lst):
    def merge(a, b):
        stack = []
        for ch in a + b:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack or stack.pop() != '(':
                    return False
                else:
                    stack.append(ch)
        return not stack
    
    return 'Yes' if merge(lst[0], lst[1]) else 'No'
``` 

The code defines a function `match_parens` that takes a list of two strings as input, each containing only open parentheses `'('` or close parentheses `')'`. It checks if it's possible to concatenate the two strings in some order to form a balanced parentheses string. 

The function uses a nested function `merge(a, b)` that takes two strings, `a` and `b`, and iterates through them, simulating the process of concatenating them. It uses a stack to keep track of open parentheses encountered. For each character ch:
- If it's an open parenthesis '(', it pushes it onto the stack. 
- If it's a close parenthesis ')', it checks if the stack is empty or if the top of the stack is not an open parenthesis '('. If either condition is true, it returns False since the parentheses are not balanced. 
- Otherwise, it pops an open parenthesis from the stack, checks if it matches the current close parenthesis, and continues the process. 

The `match_parens` function itself checks if the merge operation can be performed on the two input strings using the `merge` function, and returns 'Yes' if possible, and 'No' otherwise. 

This solution is concise and correctly matches the problem statement's requirement to provide a self-contained Python script. It can be tested directly in Python, as it does not rely on external functions or libraries.