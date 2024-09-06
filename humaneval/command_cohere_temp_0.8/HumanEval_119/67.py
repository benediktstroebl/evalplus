```python
def match_parens(lst):
    planar = [el for el in lst if el == '('] + [el for el in lst if el == ')'][::-1]
    return 'Yes' if len(planar) % 2 == 0 else 'No'
```

The logic is based on the idea that if we visualize the problem in 2 dimensions, the strings from the list can be placed one on top of another in a single plane, and in this plane, open parentheses '(' must be balanced with close parentheses ')' so that the number of '(' and ')' is the same in every zone of the plane. The function returns 'Yes' if it's possible to do that in any arrangement of the given strings in the plane, and 'No' otherwise.