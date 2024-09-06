```python
def match_parens(lst):
    open_ptr = 0
    for char in lst[1]:
        if char == '(':
            open_ptr += 1
        elif char == ')':
            open_ptr -= 1
        if open_ptr < 0:
            return "No"
    if open_ptr == 0:
        return "Yes"
    else:
        return "No"
```

The approach uses a counter to track the balance of open parentheses as it iterates through the second string. If the balance ever goes negative, there is no valid way to concatenate the strings, resulting in "No". Otherwise, if the balance is zero at the end, it's a valid concatenation and "Yes" is returned.