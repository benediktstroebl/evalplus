```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates groups of open parentheses ( ), balanced each with a set of closing parentheses, 
    without nested ones. Returns a list of separate strings.
    """
    specific test case: 
    Input: 
    "( ) (( )) (( )( ))"
    Expected Output:
    ['()', '(())', '(()())']
    """
    # Ensure only one opening parenthesis
    if not s.count('('):
        raise ValueError("Input is not well formatted!")
    # Build list of strings
    group_strings = []
    while '(' in s:
        group = ''.join(s[i:])
        group_strings.append(group)
        s = s.replace('(', '')
        open(')', '\n')
        i+=1
    return group_strings
```