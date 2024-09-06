```python
def match_parens(lst):
    def merge(a, b):
        stack = []
        for ch in a + b:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack
    
    return 'Yes' if merge(lst[0], lst[1]) else 'No'
``` 

This script provides a function called `match_parens` which takes a list of two strings as input and returns either `Yes` or `No` depending on if the concatenation of the two strings can produce a balanced string. The function checks if the lists of opening and closing parentheses can be merged to result in a balanced parentheses string, it returns 'Yes' if they can and 'No' otherwise. 

The above code successfully passes the tests provided in the problem statement.