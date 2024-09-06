```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all parenthesis groups and return as a list of separate strings.
    """
    balanced = False
    parenthesis_list = []
    for w in s:
        if w == '(' and not balanced:
            parenthesis_list.append(')')
            balanced = True
        elif w == ')' and balanced:
            parenthesis_list.append(')')
            balanced = False
        elif w == '(' and balanced:
            parenthesis_list.append(')')
            balanced = True
        elif w == ')':
            parenthesis_list.append(w)
            balanced = False
        else:
            parenthesis_list.append(w)
    return parenthesis_list
```
The function takes a string s as input and returns a list of separate strings. The function uses a backtracking approach to separate the parenthesis groups. It uses a balanced variable to keep track if the current character is an open parenthesis “(