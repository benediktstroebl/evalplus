Here's the self-contained Python script that solves the problem of separating parentheses into groups:
```python
def separate_paren_groups(s):
    # Create a list to store the group
    groups = []
    
    # Loop through each character in the string
    for c in s:
        # If it's a left parenthesis, add it to the current group and skip to the next group
        if c == '(':
            groups.append(c)
            continue
        # If it's not a left parenthesis, add it to the next group
        else:
            groups.append(c)
    
    # Return the list of groups
    return groups

# Test cases
tests = [
    "Input: '() (( )) (( )( ))'
    Output: ['()', '(())', '(()())']
    
    # Basic test cases
    tests.test = [list(map(str.maketransent, ('(', ')'), [True, False]))
    assert separate_paren_groups(tests) == ['()', '()()', '()()()]
    
    # Test case with nested parentheses
    tests = "((()))"
    assert separate_paren_groups(tests) == ['()', '()()]
```
This script defines a function **`separate_paren_groups`** that takes a string s as input and splits it into a list of groups based on parentheses. The function works by iterating through each character c in the string s. It treats a open parentheses