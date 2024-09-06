from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT: You'll want to make use of a stack to solve this problem.
    # TODO [PART A]
    # Implement and comment out the get_balanced_expression_list function below.
    # This function should take a string containing multiple nested balanced parentheses groups and
    # return a list of strings of each balanced group.
    # IMPORTANT, you should not use the built-in balanced parenthesis checking method in python!
    # This is a learning exercise, so you should implement your own stack-based algorithm to determine
    # if the parentheses are balanced.
    pass
    """
    def get_balanced_expression_list(string: str) -> List[str]:
        # HINT: You'll want to make use of a stack to solve this problem.
        pass
        return []
    """

    # TODO [PART B]
    # Now that you have a functioning get_balanced_expression_list function, use that to solve the original problem.
    return get_balanced_expression_list(paren_string)

