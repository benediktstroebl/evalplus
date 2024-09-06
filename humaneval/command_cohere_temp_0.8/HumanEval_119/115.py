```python
def match_parens(lst):
    planar = [el for el in lst if el == '('] + [el for el in lst if el == ')']
    if len(planar) % 2 == 0 and planar:
        return "Yes"
    else:
        return "No"
```
The provided solution checks whether the total number of opening parentheses `(` is equal to the total number of closing parentheses `)`. If so, it returns `"Yes"` indicating that it's possible to construct a good string. If not, it returns `"No"` indicating that it's not possible to construct a good string.