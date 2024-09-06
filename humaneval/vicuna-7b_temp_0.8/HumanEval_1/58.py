from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Helper function to match and capture groups of parentheses
    def capture_group(prefix):
        return r'\((?:\()?(?P<open>[^\)]*?)(?P<close>\))(?P<content>.*?)\)'

    # Split the input string into a list of strings
    input_list = paren_string.split()

    # Use a list comprehension to create a list of strings
    output_list = [capture(input_list[i], i) for i in range(len(input_list))]

    return output_list
