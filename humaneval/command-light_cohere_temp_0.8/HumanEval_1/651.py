```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates balanced parentheses groups into individual strings.
    Args:
        String parenthesis groups with balanced and correctly nested parentheses.
    Returns: list of individual strings.
    """
    balanced and nested grouping of parentheses.
>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Initialize empty list to store the result
    result = []

    # Iterate through each character in the string
    for char in parenthesis:
        if char == ')':
            # If the character is a right parenthesis, append an empty string to the result
            result.append('')
        else:
            # If the character is an open parenthesis, append the current result string to the result
            result.append(char)

    # Return the list of separated strings
    return result
```