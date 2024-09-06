```python
def match_parens(lst):
    # Use a counter to keep track of open parentheses
    cnt = 0
    for char in lst[0] + lst[1]:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1
        if cnt < 0:  # If the number of open parentheses is not balanced at any point
            return "No"
    if cnt == 0:  # If all parentheses are closed in the concatenated string
        return "Yes"
    else:
        return "No"
```

The approach is to concatenate the two strings and then traverse the combined string. By keeping track of '(' and ')' characters using a counter, we can determine if the parenthesis balance is maintained after concatenation. If there's any point where the counter falls below zero, it means there are more ')' characters, and the result will not be balanced, thus returning "No". Otherwise, if the counter is zero at the end of the string, it signifies a balanced outcome, returning "Yes".