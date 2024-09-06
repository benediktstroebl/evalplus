```python
def separate_paren_groups(parenthesis: str) -> List[str]:
    """
    Separates a string of parenthesis groups into individual strings.

    : Example of balanced parentheses.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    for match in parenthesis_matches(parenthesis):
        content = ''.join(match)
        result.append(content)
    return result

def parenthesis_matches(text: str) -> List[str]:
    """
    Creates a list of matches of balanced parentheses from the input string.

    >>> parenthesis_matches('()')
    ['()']
    """
    patterns = r'\(\[.*?\])|(\)\((.*?)\)'
    matches = re.sub(patterns, text, '', 'g').all()
    return matches
```