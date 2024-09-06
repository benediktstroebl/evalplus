```python
def match_parens(lst):
    # Use a counter to keep track of open parentheses
    cnt = 0

    for char in lst[0] + lst[1]:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1

        if cnt < 0:  # Unbalanced
            return 'No'

    return 'Yes'
```

This approach uses a counter to keep track of open parentheses as it iterates through the two strings. If at any point the counter dips into the negative, the function returns 'No' as there is no way to balance the parentheses. Otherwise, it returns 'Yes'.