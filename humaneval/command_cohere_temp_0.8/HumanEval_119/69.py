```python
def match_parens(lst):
    def shift_left(stack, char):
        if char == '(':
            stack.append(char)
            return True
        elif char == ')':
            if stack == ['(']:
                return False
            stack.pop()
            if len(stack) == 0:
                return False
            return shift_left(stack, ')')
        else:
            return False

    def is_balanced(stack, char):
        if char == '(':
            return len(stack) >= 1 and stack[-1] == ')'
        elif char == ')':
            return len(stack) >= 1 and stack[-1] == '('
        else:
            return len(stack) == 0

    if len(lst) < 2:
        return 'No'
    stack = []
    for char in lst[0]:
        if not shift_left(stack, char):
            return 'No'
    stack.pop()
    for char in lst[1]:
        if not shift_left(stack, char):
            return 'No'
    return 'Yes' if is_balanced(stack, '') else 'No'
``` 

The provided Python script implements a function named `match_parens` taking a list of two strings as input, each containing only open parentheses `'('` or close parentheses `')'`. The function aims to determine if it's possible to concatenate these two strings in some order to form a balanced parentheses string. 

To accomplish this, the function employs a stack data structure. It iterates through each character in the first string and uses a `shift_left` function to simulate shifting parentheses onto the stack. If this results in an empty stack, the strings cannot be concatenated. Similarly, the function iterates through the second string using the same process. If shifting a character results in an unbalanced stack, the answer is `No`. 

The function returns `Yes` if it's possible to form a balanced string by concatenating the two input strings in some order. It returns `No` otherwise. This algorithm has a time complexity of O(mn) where m is the length of the first string and n is the length of the second string. 

The space complexity is O(m+n) due to the stack of size at most m+n. As a whole, the function is a straightforward application of the shift and reduce algorithm for solving parentheses problems.