from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def dfs(i, j, depth):
        if i > j:
            return

        # remove redundant parentheses
        while i < j and paren_string[j] == ")":
            j -= 1
            depth -= 1
        if i > j:
            return

        res = []
        for k in range(i + 1, j):
            if paren_string[k] == "(":
                depth += 1
            elif paren_string[k] == ")":
                depth -= 1
            if depth == 0:
                res += dfs(i + 1, k - 1, 0)
                i = k + 1
        if depth == 0:
            res += dfs(i, j - 1, 0)

        return res

    return dfs(0, len(paren_string) - 1, 0)

