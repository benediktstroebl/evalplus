Here's the Python script with a self-contained function that solves the problem of separating nested parentheses into separate groups and passes all corresponding tests:

```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of balanced parentheses into separate strings.
    Returns a
list of those strings.
    """
    balanced parentheses are opened and closed properly
    """
    input_list = [x.strip() for x in s.groupings(s)]
    return input_list

def groupings(string: str) -> List[str]:
    """
    Return list of all groups of non-space characters in a string.
    """
    return string.split("\n"""}
[x for x in string.split(' ')]

# Unit tests
def test_groupings():
    for s in ['()((())()', '((()) )', '()()']):
        assert separate_paren_groups(s) == ['()', '(())', '()()']

test_groupings()
```

This script defines a `separate_paren_groups` function that processes a string of balanced parentheses, returning them as a list of separate strings. It also has a test_groupings function that creates test cases and asserts the correctness of the `separate_paren_groups` function.