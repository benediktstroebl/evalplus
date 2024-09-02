from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []

    # check for errors in the string, if error, return empty list
    open_braces, close_braces = 0, 0

    for i, char in enumerate(paren_string):
        if char == '(':
            open_braces += 1
        elif char == ')':
            close_braces += 1
        if open_braces < close_braces:
            return []

    # if no error, continue
    # We'll start at the first char and do a DFS to find all groups
    # DFS
    # create a list to append to, and start with the first character, as it may or may not be an open paren
    # if the first char is a close paren, return
    # if the first char is an open paren, and the next is a close paren, return
    # if the first char is an open paren, and the next is not a close paren, go to step 4
    # 4. iterate through the string and find matching closing braces, keeping track of how many
    #    if the next char is an open brace, and the number of matching close braces is equal to the total
    #    then, append the current string to our list
    #    else, skip the next char and continue
    # 6. return the list of groups
    # if there is only one group, return that group
    # if there are no groups, return empty list
    groups = []

    def dfs(string, i):
        if i == len(string):
            return
        if string[i] == ')':
            return

        if string[i] == '(':
            if i + 1 == len(string):
                return
            if string[i + 1] == ')':
                return

            open_braces = 0
            close_braces = 0
            j = i + 1
            while j < len(string):
                if string[j] == '(':
                    open_braces += 1
                elif string[j] == ')':
                    close_braces += 1
                if
