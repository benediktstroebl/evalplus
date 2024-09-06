Certainly! Here is the Python script that includes the self-contained function `separate_paren_groups`, which is designed to solve the problem of separating and unravelling parenthesis groups:
```python
# Function to separate and unroll parentheses
def separate_paren_groups(parenthes: str) -> List[str]:
    """
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    for match in parenthes.match_groups(parenthes):
        result.append(match[::-1])
    return result

# Helper function to match and split groups of parentheses
def match_groups(text: str) -> List[str]:
    """
    >>> match_groups('( ) (( )) (( )( ))')
    ['(', ')', '(())', '(()())']
    """
    import re
    return re.sub(r'([('([({[-+\s]+?]()+)', 1)])', r'\1\2', text)

tests = {
    'Input: ((()))', should return []',
    'Input: ( ()() )', should return ['()', '()()'],
    'Input: (() )', should return ['()'],
    'Input: ( ( ) )', should return ['()', '()'],
    'Input: ( ( ( ) ) )', should return ['()', '()', '()'],
    'Input: ( ( ( ( ) ) ) )', should return ['()', '()', '()', '()'],
    'Input: (( ( ) ) )', should return ['(', ')', '()', '()'],
    'Input: (( ))', should return ['()']
}

# Run the function on each test case
for test in tests:
    print(separate_paren_groups(test))
``` 
The function, `separate_paren_groups`, has been modified to include a new helper function, `match_groups`. This function is designed to use the regular expression to match and split the groups of parentheses in a given text string. The main function takes the new input, processes it, and returns the result as a list of strings.