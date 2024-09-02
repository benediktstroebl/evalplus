from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def is_balanced_group(input_group: str) -> bool:
        """ Return True if the input string is a balanced group. """
        if len(input_group) % 2 == 1:
            return False
        stack = []
        for c in input_group:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack

    def find_next_balanced_group_start_index(input_string: str) -> int:
        """ Find the index of the first balanced group starting at the provided index.
        """
        idx = 0
        while idx < len(input_string):
            balanced_group_start = idx
            while idx < len(input_string) and input_string[idx] != "(":
                idx += 1
            if idx == len(input_string):
                return -1
           
