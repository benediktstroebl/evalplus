from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # if you use any Python libraries, make sure to include them in your code comments.
    # you may need to make use of the split() and count() methods
    # when writing your code, please use the test cases provided.
    # make sure to write your code in the separate_paren_groups function
    # to properly check your code, run the following command from the command line:
    # run 'python3 -m doctest -v <filename>'
    # e.g. 'python3 -m doctest -v 2021_02_09_practice.py'

    groups = []

    paren_groups = paren_string.split()

    for i in range(0, len(paren_groups)):
        group = paren_groups[i]

        count = group.count("(") - group.count(")")

        if count == 0:
            groups.append(group)

    return groups
