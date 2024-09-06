```python
def separate_paren_groups(s: str) -> List[str]:
    result = []
    for group in s.group():
        opening_brace = group[0]
        if opening_brace.isspace():
            closing_brace = ')'
        else:
            closing_brace = group[group.isspace(): '('
            result.append(opening_brace)
        result.append(closing_brace)
    result.append(' ') *continue

    return result
``` 
This function takes a string as input and loops through each group of parentheses, separating the group into individual strings. It handles the space characters by adding a space character after the closing parenthesis. The function returns a list of strings.