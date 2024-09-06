```python
def parse_nested_parens(s: str) -> List[int]:
    """
    This function aims to parse a string of nested parentheses and return the deepest level of nesting.
    :param s: The string to parse
    :return: list of levels of nesting in parentheses
    """
    # Split the string by spaces into a list of substrings
    substrings = s.split()
    biggest, level = 1
    parsed_level = []
    for sub in substrings:
        # if sub is empty, ignore it
        if sub == '':
            continue
        # Otherwise, check if it is a valid opening parent
        elif sub == '(':
            parsed_level.append(level)
            level += 1
        # Otherwise, check if it is a valid closing parent
        elif sub == ')':
            level -= 1
        # If we made it to the opening parent and are not closing, ignore the current substring
        elif sub == '):':
            continue
        else:
            # any other character is invalid
            raise ValueError("Invalid characters in parentheses")
    return parsed_level
```