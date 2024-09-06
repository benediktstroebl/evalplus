```python
def match_parens(lst):
    def check(s, tail):
        if not tail:
            return True
        if s == '(':
            return tail == ')'
        if s == ')' and tail == '(':
            return True
        return False
    if len(lst) != 2:
        return "Invalid input"
    s, tail = lst
    if s == tail:
        return "No"
    if check(s, tail) or check(tail, s):
        return "Yes"
    return "No"
```

The code defines a function `match_parens` that takes a list of two strings as input, and returns "Yes" if it's possible to concatenate the strings in some order to form a balanced parentheses string, and returns "No" otherwise.

It includes a helper function `check` that checks if a string `s` followed by a tail end can form a balanced parentheses string.

To solve the problem, it first checks if the input list has exactly 2 elements, and then checks if the two strings are identical, returning "No" instantly if so. Then, it uses the `check` function to verify if the two strings can form a balanced string when concatenated in each possible order, returning "Yes" if any combination is valid, and "No" otherwise.