from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Your code here
    # return_list = []
    #
    #
    #     i = 0
    #     # increment i until it is greater than length of input
    #     while i <= len(paren_string):
    #         # make a new string that is one character long.
    #         # set it to an empty string.
    #         temp_string = ""
    #         # increment i by one.
    #         i += 1
    #         # append temp_string to return_list.
    #         # return_list.append(temp_string)
    #         # if i is greater than the length of the input string, we are done.
    #         if i > len(paren_string):
    #             break
    #
    #         # add the first character of the input string to temp_string.
    #         # temp_string = paren_string[0]
    #         # remove the first character of the input string.
    #         paren_string = paren_string[1:]
    #
    #         # while the
