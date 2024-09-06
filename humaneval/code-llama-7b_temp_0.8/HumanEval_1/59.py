from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # arr = []
    # bracket = 0
    # for i in paren_string:
    #     if i == "(":
    #         bracket += 1
    #     if i == ")":
    #         bracket -= 1
    #     if bracket == 0:
    #         arr.append(paren_string[:i+1])
    #         paren_string = paren_string[i+1:]
    #         bracket = 0
    # return arr

    def parse(s: str) -> List[str]:
        # base case: empty string
        if not s:
            return []

        # initialize variables
        count = 0
        max_idx = 0
        string = ""

        for i, char in enumerate(s):
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1

            # if we reach the end of the group, save it and start a new one
            if count == 0:
                max_idx = i + 1
                break

        # save string, recurse on the remaining part of the string
        return [s[:max_idx]] + parse(s[max_idx:])

    return parse(paren_string)

