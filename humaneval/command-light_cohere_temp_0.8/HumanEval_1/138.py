```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate groups of parentheses into separate strings.
    Returns list of strings.
    """ Tests to test with any spaces
    """
    result = []
    for match in parentheses:
        pattern = r"\(([^()]*\))"
        if match.count(pattern.findall(match): > 0):
            result.append(match[pattern.findall(pattern)[0])
    return result
``` 
This function takes a string of parentheses as input and returns a list of strings, each separated by a matching pair of parentheses. The function also handles any empty strings gracefully.