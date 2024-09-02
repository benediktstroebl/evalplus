from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []

    def recurse_paren(paren_string: str) -> List[str]:
        """
        This function will pop off the first ( and return a string of the nested parentheses
        :param paren_string:
        :return:
        """
        result = []
        if paren_string.startswith('('):
            start = 1
        else:
            start = 0
        if start >= len(paren_string):
            return result
        for i in range(start, len(paren_string)):
            if paren_string[i] == '(':
                result.append(paren_string[start:i+1])
                break
        while True:
            paren_string = paren_string[i+1:]
            if paren_string.count(')') < paren_string.count('('):
                return result
            else:
                recursive_result = recurse_paren(paren_string)
                if len(recursive_result) == 0:
                    break
                else:
                    result.append(recursive_result)
                    i += len(recursive_result)
        return result
    recurse_paren(paren_string)
    return result
