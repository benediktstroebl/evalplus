

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # start by defining a method that checks for balanced parentheses
    def is_paren_balanced(string: str) -> bool:
        """Returns true if a string of parentheses is balanced, otherwise false.
        Ignores spaces
        >>> is_paren_balanced('( ) (( )) (( )( ))')
        True
        >>> is_paren_balanced('((()')
        False
        """
        # start with a list that will hold the opening parenthesis positions
        opening_paren_positions = []

        # iterate through the characters in the string
        for pos, char in enumerate(string):
            # if we encounter an opening parenthesis
            if char == '(':
                # append the position to the list
                opening_paren_positions.append(pos)
            # if we encounter a closing parenthesis
            if char == ')':
                # if there are any elements in the list
                if opening_paren_positions:
                    # pop the last element in the list and see if it is the
                    # corresponding open parenthesis
                    if string[opening_paren_positions.pop()] == '(':
                        # if it is, then the parentheses are balanced
                        continue
                    # otherwise, the parentheses are not balanced
                    return False
                # if the list is empty, then there are not matching closing
                # parentheses
                return False

        # if we finish iterating through all characters
        # if the list is empty, then the parentheses are balanced
        if opening_paren_positions == []:
            return True
        # otherwise, there are unmatched open parentheses
        return False

    # start by defining a method that separates the parentheses into groups
    def separate_paren_groups(string: str) -> List[str]:
        """Returns a list of parentheses groups.
        Each group is a separate string of balanced parentheses.
        Ignores spaces
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
        """
        # start with an empty list
        groups = []

