```python
def match_parens(lst):
    def expand(s, stack):
        if not s:
            return True
        if s[-1] == '(':
            stack.append(s)
            return expand(s[:-1], stack)
        elif s[-1] == ')':
            if not stack or stack.pop()[-1] != '(':
                return False
        return expand(s[:-1], stack)
    
    return 'Yes' if all(map(expand, lst)) else 'No'
``` 

The solution involves using a recursive expansion of parentheses, which recursively expands the parentheses while keeping track of the stack of parentheses that have been opened but not yet closed. The overall structure is a list comprehension that maps the expand function to each list element, and then uses the all function to check if all expansions are valid.

The expand function goes through the string and each opening parenthesis '(' it encounters, it pushes the current string onto a stack and recursively expands the rest of the string. If it encounters a closing parenthesis ')', it checks if the stack is empty or if the top string on the stack does not begin with an opening parenthesis. If either of these conditions is true, then the expansion is invalid, and the function returns False. Otherwise, it pops the top string from the stack, concatenates it with the current string, and continues expanding the rest of the string.

To use this function, you can call it with a list of strings as input, and it will return 'Yes' if it is possible to concatenate the strings in some order to create a balanced parentheses string, and it will return 'No' otherwise.  This approach has a time complexity of `O(n^2)` due to the nested recursion and string concatenation. 

This solution is based on the fact that the expansion of a valid string of parentheses will always end, and it's described in this explanation: https://leetcode.com/problems/balance-a-string/discuss/95326/A-simple-and-straightforward-recursive-approach.