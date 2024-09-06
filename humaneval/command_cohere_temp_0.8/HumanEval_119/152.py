```python
def match_parens(lst):
    open_tup = tuple(char for char in lst[0] if char == '(')
    close_tup = tuple(char for char in lst[1] if char == ')')
    return "Yes" if open_tup and close_tup and len(open_tup) == len(close_tup) else "No"
```

This approach creates tuples of open and close parentheses and directly compares their lengths. If the lengths are equal, the answer is "Yes"; otherwise, it's "No". This works because the problem statement states that the strings consist of only parentheses and, therefore, a string of parentheses can be considered "balanced" if the number of open parentheses is equal to the number of close parentheses and vice versa. 

Here is a simpler solution:
```python
def match_parens(lst):
    return "Yes" if len(lst[0]) == len(lst[1]) else "No"
```

This solution assumes that the strings contain only parentheses and simply checks their lengths. It considers the problem solved if the list has the same number of parentheses as another. Again, this works because the problem statement implies that the strings contain only parentheses.