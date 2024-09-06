```python
def separate_paren_groups(parenthesis_string: str) -> List[str]:
    """Separate groups of parentheses into separate strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    pattern = r"\(([^()]+)\)"
    return [match.split(pattern)[0] for match in re.search(pattern, parenthesis_string)]
``` 
This Python code defines a function called `separate_paren_groups` that separates and returns a list of non-nested parentheses from a given string. The function uses the string pattern `(\(([^()]+)\))` to identify and split each group of parentheses in the input string.