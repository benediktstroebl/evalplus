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
    # We need to have an overall function that will call a helper function on every element of a list
    # We will need to define 2 helper functions
    # # Check whether the bracket is open or closed
    # # Keep track of the opening and closing brackets
    # # On checking the last element of a list of brackets, return the list
    # # Need a "main" function to call helper functions
    # # Check the length of the list
    # # If it is 0 return an empty string
    # # If it is not, proceed to call the helper functions on the list
    # # If it is 1, check whether it is open or closed
    # # If it is closed, append the list
    # # If it is not, call the helper function on that element
    # """

    def check_brackets(brackets):
        """Check the length of the list of brackets.
        If it is 0 return an empty string.
        If it is not, proceed to call the helper functions on the list"""
        if len(brackets) == 0:
            return ""
        else:
            return helper(brackets, 0, "")

    def helper(brackets, index, output):
        """Check the length of the list of brackets.
        If it is 0 return an empty string.
        If it is not, proceed to call the helper functions on the list"""
        if len(brackets) == 0:
            return output
        elif brackets[index] == "(":
            index += 1
            output += "("
            return helper(brackets, index, output)
        elif brackets[index] == ")":
            index += 1
            output += ")"
            return helper(brackets, index, output)

    def count_brackets(brackets):
        """This function counts the number of brackets in a list
        :param brackets: a list of brackets
        :return: an integer representing the number of brackets in the list
        """
        counter = 0
        for bracket in brackets:
            if bracket == "(":
                counter += 1
            elif bracket == ")":
                counter -=
