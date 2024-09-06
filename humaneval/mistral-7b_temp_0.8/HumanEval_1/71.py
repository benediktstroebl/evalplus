from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # First, make a list of all the paren pairs and then loop through them to see if they are valid
    # You should be able to do this in O(n) time
    # Consider using the re module
    # Hint: use the re.findall function
    # Dont forget to ignore spaces
    paren_pairs = re.findall('()', ' '.join(paren_string.split()))

    # Now make a list of all the valid paren groups
    paren_groups = []
    for paren_pair in paren_pairs:
        if is_valid_paren_group(paren_pair):
            paren_groups.append(paren_pair)

    # Return the list of valid paren groups
    return paren_groups

