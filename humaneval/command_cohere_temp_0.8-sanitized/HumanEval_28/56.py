import typing
def concatenate(strings: typing.List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result