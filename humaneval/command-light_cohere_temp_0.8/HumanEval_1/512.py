Here's the self-contained Python script that solves the problem of separating out balanced parentheses:
```python
def separate_paren_groups(string):
    # Function to separate balanced parentheses into a list of strings.
    groups = []
    for match in string.match(/([ )]+|\([ ]+(\))?\g):
        # Add the current group to the list
        groups.append(matchgroup())
        # Return the list of strings
    return groups

# Unit tests
def test_separate_paren_groups():
    # Sample input string
    input_str = "( ) (( )) (( )( ))"
    
    # Function call
    result = separate_paren_groups(input_str)
    
    # Verify the output
    assert len(result) == 4
    assert result[0] == '()'
    assert result[1] == '()'
    assert result[2] == '()'
    assert result[3] == '(())'
```
This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated strings. The script also includes unit tests to verify the correctness of the `separate_paren_groups` function.