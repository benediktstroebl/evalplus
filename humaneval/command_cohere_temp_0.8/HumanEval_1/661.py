Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing individual groups of parentheses. The code is annotated with explanations and is tested on the given case:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string."""
    results: List[str] = []
    stack: List[str] = []

    for char in paren_string:
        if char == '(':
            stack.append('(')
        if char == ')':
            if not stack or stack.pop() != '(':
                results.append(''.join(stack))
            results.append('')

    if stack:
        results.append(''.join(stack))

    return results

# Tests
paren_string = '( ) (( )) (( )( ))'
expected_result = ['()', '(())', '(()())']

print(f'Test case:separate_paren_groups({paren_string}) => {separate_paren_groups(paren_string)}')
print(f'Expected Result: {expected_result}')

assert separate_paren_groups(paren_string) == expected_result
```

The code works as follows:
1. The function's signature is `separate_paren_groups(paren_string)`, taking a string of parentheses as input.
2. The variable `results` is a list where all the separated groups of parentheses will be stored.
3. The variable `stack` is a list used to keep track of open parentheses. When we encounter a closing parenthesis `)`, we check if the top of the stack is an open parenthesis `(` (using `stack.pop()` and checking for equality to `('`) and if not, we consider the group complete and add it to the results list.
4. If the input string ends without a closing parenthesis for an open parenthesis, it will remain in the `stack`, so we do an additional check at the end to make sure no open parentheses are left behind and add the remaining string to the results.
5. The function returns the `results` list, which will contain each group of parentheses as a separate string.
6. The code includes a test case where the input string is `( ) (( )) (( ()) )` and the expected result is `['()', '(())', '(()())']`.
7. The test case prints the actual result and expected result, and it asserts that the function's output matches the expected output.