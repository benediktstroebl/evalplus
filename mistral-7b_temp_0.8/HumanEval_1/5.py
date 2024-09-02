from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Here are some useful functions from python
    # https://docs.python.org/3/library/functions.html
    # print(paren_string)
    # list_of_groups = []
    #
    # if paren_string.find('(') == -1:
    #     list_of_groups.append(paren_string)
    #
    # index = 0
    # while paren_string.find('(') != -1:
    #     index = paren_string.find('(')
    #     list_of_groups.append(paren_string[0:index])
    #     paren_string = paren_string[index+1:]
    #     if paren_string.find(')') == -1:
    #         list_of_groups.append(paren_string)
    # return list_of_groups

    # Here are some built-in list functions
    # https://docs.python.org/3/tutorial/datastructures.html#list-type-objects

    list_of_groups =
