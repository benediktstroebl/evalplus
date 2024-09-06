```python
def match_parens(lst):
    cnt_open = 0
    for char in lst[1]:
        if char == '(':
            cnt_open += 1
        elif char == ')':
            cnt_open -= 1
        if cnt_open < 0:
            return "No"
    if cnt_open == 0:
        return "Yes"
    else:
        return "No"
```

The code defines a function `match_parens` that takes a list `lst` with two strings as its elements. The function iterates through the second string using a `for` loop. It counts the open parentheses `'('` and subtracts the count of closed parentheses `')'` it encounters. If the count of open parentheses is negative at any point, it returns "No" since it is impossible to construct a balanced string. If the total count of open parentheses is zero after processing all characters, it returns "Yes" as it is possible to construct a balanced string. If neither of these conditions is met, it returns "No." 

**Time complexity**: `O(n)` where `n` is the length of the second string.
**Space complexity**: `O(1)` as it only uses a constant amount of space to store the counter.