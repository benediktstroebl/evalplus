```python
def separate_paren_groups(paren_string: str) -> List[str]:
    open_parens = {'('}
    closed_parens = '))'
    result = []

    for char in paren_string:
        if char in open_parens:  # starts with open paren
            result.append(char)
        elif char in closed_parens:   # ends with closed paren
            result.append(char)
        else:  # other character, just add space
            result.append(' ')

    return result
```
This Python function called `separate_paren_groups` takes a string of parentheses as input and returns a list of separated parentheses. The function uses two dictionaries, `open_parens` and `closed_parens`, to know the difference between open and closed parentheses. It uses a manual space as a separator to ensure balanced spacing around each pair of parentheses. The function works by iterating over each character in the input string and adding the character to the result string if it is either an open parent or a closed parent. If the character is neither an open or closed parent, it simply adds a space to maintain consistent spacing.