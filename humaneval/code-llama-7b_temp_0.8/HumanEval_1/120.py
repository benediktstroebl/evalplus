from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    """BEGIN PSEUDOCODE"""
    # while(str[i] is not an open brace)
    #     while(str[i] is not an open brace)
    #         if(str[i] is not an open brace)
    #             print str[i]
    #             increment i
    #         else
    #             increment i
    #         while(str[i] is an open brace)
    #             if(str[i] is not an open brace)
    #                 print str[i]
    #                 increment i
    #             else
    #                 increment i
    #         print str[i]
    #         increment i

    #     print str[i]
    #     increment i
    #     while(str[i] is an open brace)
    #         if(str[i] is not an open brace)
    #             print str[i]
    #             increment i
    #         else
    #             increment i
    #     print str[i]
    #     increment i

    #     while(str[i] is an open brace)
    #         if(str[i] is not an open brace)
    #             print str[i]
    #             increment i
    #         else
    #             increment i
    #
    #     print str[i]
    #     increment i
    #     while(str[i] is an open brace)
    #         if(str[i] is not an open brace)
    #             print str[i]
    #             increment i
    #         else
    #             increment i
    #     print str[i]
    #     increment i

    """END PSEUDOCODE"""

    groups: List[str] = []
    group: List[str] = []
    open_brace_count: int = 0
    index: int = 0
    while index < len(paren_string):
        if paren_string[index] == '(':
            open_brace_count += 1
            group.append(paren_string[index])
        elif paren_string
