```python
def match_parens(lst):
    def check(s, curr_open, curr_close):
        if not s:
            return True
        if s[0] == '(':
            curr_open += 1
        elif s[0] == ')':
            curr_close += 1
        if curr_open > curr_close:
            return False
        if curr_open < curr_close:
            return check(s[1:], curr_open, curr_close)
        return check(s[1:], curr_open, curr_close)
    
    if lst[0] == lst[1]:
        return 'Yes'
    return check(lst[0], 0, 0) and check(lst[1], 0, 0) and 'No'
```

The code defines a function `match_parens` that takes a list of two strings as input and returns 'Yes' if it is possible to concatenate the strings in some order to create a balanced and valid parentheses string. It returns 'No' otherwise.

The base case checks if the two strings are equal, and if so, returns 'Yes' since they can be concatenated in the simplest order. 

The recursive portion of the code is defined in a check function that takes a string s, an open parentheses counter curr_open, and a close parentheses counter curr_close. 

It follows these steps:
1. If the string is empty, it returns True.
2. If the string starts with an open parenthesis '(', it increments the open parentheses counter. 
3. If the string starts with a close parenthesis ')', it increments the close parentheses counter. 
4. It checks if the open parentheses counter is greater than the close parentheses counter. If so, it returns False as the string would end with an unmatched open parenthesis.
5. If the open counter is less than the close counter, it returns the result of a recursive call to check with the remaining string sliced from the first character. This allows the function to explore all possible combinations of parentheses.
6. If the open parentheses counter is equal to the close parentheses counter, it returns the result of a recursive call to check with the remaining string sliced from the first character.

Finally, the match_parens function uses the check function to verify if it is possible to construct a valid parentheses string using both input strings, and returns the corresponding result.