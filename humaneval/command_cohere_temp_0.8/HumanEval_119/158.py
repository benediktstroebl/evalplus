```python
def match_parens(lst):
    def merge(a, b):
        stack = []
        for c in a + b:
            if c == '(':
                stack.append(c)
            else:
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack
    
    return 'Yes' if merge(lst[0], lst[1]) else 'No'
``` 

This script provides a clear and concise function that solves the problem with descriptive variable names like `merge` to explicitly express the action of merging two strings of parentheses and checking if it results in a balanced parentheses chain.