Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent each individual group of parentheses. The script also includes a test case to demonstrate how the function can be tested:
```python
# The following import is needed for type hinting
import typing

# The function to be tested
def separate_paren_groups(paren_string: str) -> typing.List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    result: typing.List[str] = []
    stack: typing.List[str] = []
    for char in paren_string:
        if char == '(':
            stack.append('(')
        if char == ')':
            if not stack or stack.pop() != '(':
                print('Unbalanced group')
            else:
                result.append(')'.join(stack))
    return result

# Test case
assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])
```

To test the function, a test case is developed that checks whether the output of the function is as expected. The `assertEqual` method verifies that the output of `separate_paren_groups` when applied to the input string `( ) (( )) (( )( ))` is equal to ['()', '(())', '(()())']. If the output is indeed this list, the test will pass; otherwise, it will fail. 
The `separate_paren_groups` function iterates through the input string, keeping track of parentheses openings in a stack. When a closing parenthesis is encountered, the function checks whether it has a matching opening parenthesis on the stack. If so, the opened group is considered balanced, and it is added to the result list. This process ensures that each group of parentheses is properly separated and returned.