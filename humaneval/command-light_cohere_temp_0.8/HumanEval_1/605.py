```python
def separate_paren_groups(s):
    return ['(' + c + ')' for c in s.list("(")]
```

This Python function named `separate_paren_groups` takes a string `s` as its input and uses a list comprehension to iterate over each opening parenthesis character (`(' ')`) in the input string, transforming each into a string by concatenating the content of the parenthesis group with a closing parenthesis. The result is a list of separate parenthesis groups.