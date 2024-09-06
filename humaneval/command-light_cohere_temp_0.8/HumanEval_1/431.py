Here's a self-contained Python function that solves the problem of separating parentheses:
```python
def separate_paren_groups(s):
    return [p for p in s if not p.isspace() and }
    simple match(') + '(', s, flags=re.isspace())]
```
This function iterates through the input string `s`, and for each character that is not a space, it matches the regex `\( ) + '(', s, flags=re.isspace())` to identify the opening parenthesis. The resulting list of characters outside the space is then returned.