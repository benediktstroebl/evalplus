```python
def separate_paren_groups(s):
    # type: str
    return ['(' + c + ')' for c in s.
    # ['.replace(',)', ' ')
    # ensure balanced closing by only adding closing parenthesis)
    # remove extra spaces
    return [c for c in s.replace(' ') if c != '(']
```
 The function takes a string s as input and splits it into groups of parentheses, separating each group by adding a single closing parenthesis. The output is a list of these strings.