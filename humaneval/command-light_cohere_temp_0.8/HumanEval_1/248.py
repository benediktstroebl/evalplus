Here is a self-contained Python script that solves the problem of separating out different groups of parentheses in a given string:
```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate groups of well-formed parentheses into a list of strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [brace.format(''.join(braces) for braces in zip(['(')'.split(), ['()'.split(), '))'.split()])
```
This code defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings with properly separated parentheses. The code uses a `zip` to split the input into different groups of parentheses, and then uses a list comprehension to `join` each group into a single string. Then, the `brace.format` function to make this string a list of brace groups into a balanced format, ensuring that each open brace is properly closed.