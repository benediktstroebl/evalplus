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
        return check(s[1:], curr_open, curr_open)
    
    if lst[0] == lst[1]:
        return 'Yes'
    return 'No' if check(lst[0] + lst[1], 0, 0) else match_parens(lst[1:])
```

The provided code defines a function `match_parens` that takes a list of two strings as input, where each string contains only opening parentheses `'('` or closing parentheses `')'`. The function checks if it's possible to concatenate these two strings in some order to create a balanced string with equal numbers of opening and closing parentheses. 

It achieves this by using a recursive helper function `check` that tracks the current count of opening and closing parentheses. If the balance of parentheses is ever incorrect, it returns `False`. If the input string is empty, it returns `True`. Otherwise, it recursively checks the rest of the string based on the next character.

The `match_parens` function first checks if the two input strings are identical; if so, it returns "Yes" right away because they can be concatenated to form a balanced string. If the strings differ, it uses the `check` function to verify if it's possible to make a balanced string by concatenating them in some order. If this is possible, it recursively calls itself with the second element of the list, which allows for checking alternative combinations of parentheses. 

The overall time complexity of the code is O(2^n), where n is the total length of the input strings, as it explores all possible combinations of parentheses.