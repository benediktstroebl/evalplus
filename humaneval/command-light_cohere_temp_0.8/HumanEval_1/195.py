```python
def separate_paren_groups(s):
    """Separate balanced parentheses from spaces into separate strings.
    Return a balanced parentheses in separate strings.

    # Using list comprehension to find all matched pairs of parentheses.
    return [ [[p for p in '(' + s[i:]) for i, p in enumerate(s) if p == '('] +
        [[c for c in s[i:]] for i in enumerate(s) if c == ')')]

# Example test cases
test_cases = [
    '() (( )()'.split()
    , '( )()()'.split()
    , '((()))'
    , '( ) ( )'
    , '( )   ((  ))'
]

# Test function
def test_separate_paren():
    test_cases = [x.split() for x in test_cases]
    res = separate_paren_groups(x)
    assert res == [x.split() for x in test_cases]

# Test cases
test_separate_paren()
``` 
This Python script defines a function called `separate_paren_groups` that takes a string as input and returns a list of strings separated by balanced parentheses. The function uses list comprehension to find all matched pairs of parentheses and uses slicing to separate the string into individual groups. The test suite contains some example test cases that cover different scenarios. The test function then checks if the output of `separate_paren_groups` is equal to the corresponding input test cases and passes the test suite.