def concatenate(strings: List[str]) -> str:
    """
    Function to concatenate list of strings into a single string and returns the result
    """
    return ''.join(''.join(strings) if strings else [])