Here's a self-contained Python function that solves the problem of separating nested parentheses:
```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of nested parentheses.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [match.strip() for match in re.match("\(\)|\([ )", "$"] in s)][::-1]
```
The function uses the regular expression `re.search()` along pattern to find the balanced groups of parentheses and returns the matched strings as a list. The backslash operator `-1` in the `[]` index ensures that the last matched group is the first one in the returned list.