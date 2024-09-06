```python
def match_parens(lst):
    open_ptr = 0
    for ch in lst[1]:
        if ch == '(':
            open_ptr += 1
        elif ch == ')':
            open_ptr -= 1
        if open_ptr < 0:
            return "No"
    if open_ptr == 0:
        return "Yes"
    else:
        return "No"
```

The provided Python script defines a function `match_parens` that takes a list `lst` as input, where each element is a string consisting of either '(' or ')' characters. The function calculates the total number of open parentheses '(' in the second string and then checks if this count is consistent with the total number of close parentheses ')' in the first string. If the count matches, the function returns "Yes," indicating that the two strings can be concatenated to form a balanced parentheses string. Otherwise, it returns "No" if the counts do not match, as there is no way to form a balanced string by concatenating the given strings.