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

    def is_balanced(string):
        stack = []
        for char in string:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
        return True

    def find_groups(paren_string):
        start = 0
        groups = []
        while start < len(paren_string):
            start = paren_string.find("(", start)
            if start == -1:
                break
            start += 1
            end = paren_string.find(")", start)
            if end == -1:
                break
            if is_balanced(paren_string[start:end+1]):
                groups.append(paren_string[start:end+1])
                start = end + 1
        return groups

    return find_groups(paren_string)

