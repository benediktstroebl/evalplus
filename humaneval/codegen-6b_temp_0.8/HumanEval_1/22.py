from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # rem is the repeated characters
    def balanced(rem):
        cnt = 1
        for r in rem:
            if r == '(':
                cnt += 1
            elif r == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0

    # look at the strings one at a time and put in the beginning of new_str, based on the following criteria:
    # if the string is balanced, put it in new_str, else if the string is balanced, repeat the string, but
    # break it at every open parenthesis
    # if the string is not balanced, put the string in new_str, break it at every open parenthesis
    # then repeat the process until you've put every string in new_str
    # thn return new_str
    def balance(string):
        new_str = ''
        parens = ['(', ')']
        buff = ''
        for c in string:
            if c in parens:
                if len(buff) == 0:
                    new_str += c
                else:
                    if balanced(buff):
                        new_str += c
                        buff = ''
                    else:
                        new_str += buff
                        buff = c
            else:
                buff += c
        if len(buff) != 0:
            new_str += buff
        return new_str

    # separate the strings into groups of balanced strings
    # then split each group into substrings
    # for each substring, remove the extra parentheses
    # thn add the substring to the list
    # return the list
    def balance_and_split(string):
        new_str = []
        sep = '()'
        buff = ''
        for c in string:
            if c in sep:
                if len(buff) == 0:
                    new_str.append(c)
                else:
                    if balanced(buff):
                        new_str.append(c)
                        buff = ''
                    else:
                        new_str[-1] += buff
                        buff = c
            else:
                buff += c
        if len(buff) != 0:
            new_str[-