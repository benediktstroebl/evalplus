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

The function `match_parens` takes in a list of two strings as its argument. It initializes a variable `cnt_open` to keep track of open parentheses encountered. The function then iterates through the characters of the second string in the list, incrementing `cnt_open` for each open parenthesis '(' and decrementing it for each close parenthesis ')'.

If at any point the value of `cnt_open` dips below zero, it means there are more close parentheses ')' than open parentheses '(' in the string, and an unbalanced string cannot be formed. In this case, the function returns "No".

After processing the second string, if the value of `cnt_open` is zero, it means all the open parentheses have been matched with close parentheses, and a balanced string can be formed. So, the function returns "Yes" in this case. If `cnt_open` is still positive, it means there are excess open parentheses, and an unbalanced string cannot be formed, so the function returns "No".