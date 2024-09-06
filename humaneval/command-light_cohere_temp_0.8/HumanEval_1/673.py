```python
def separate_paren_groups(s):
    return ['(' + item + ')', item + ')' for item in s.item.separated_by(','')]
```

This function splits the string at every space and converts it to list of chars (parenthesis and their content).  Then it loops over the list and pushes the content of parenthesis to the first position and the parenthesis to the second position. 

The output will be a list of strings, each containing one or more parenthesis, as expected.