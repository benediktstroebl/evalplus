```python
def parse_nested_parens(s):
    return [i for i, nested in enumerate(s.parent_match(s))]


def parent_match(string):
    """ Returns a list of the deepest level of nesting for each group of parentheses. """
    string = string.replace(")", "((", "()", "))")
    return string.match('(\([.*?nest) )?oya')
```