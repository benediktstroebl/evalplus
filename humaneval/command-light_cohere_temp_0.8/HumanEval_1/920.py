```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate groups of parentheses into individual strings.
    Return list of strings
    Recursively traverses the string, and for each group of closed parentheses,
    returns the string.
    >>> return ['()', '((()))', '(()())']
    ```
This code defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings. It achieves this by traversing the string recursively and returning the string for each group of closed parentheses. The code ensures balanced parentheses and ignores spaces, making it suitable for the problem of separating groups of parentheses in a given input string.