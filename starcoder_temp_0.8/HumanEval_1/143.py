from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # This function should return a list of substrings, but there's an issue
    # of what happens if there are multiple levels of parentheses.
    # For example, if we pass in '( ( ( ) ) ) )', we will want the function to return
    # ['((())', '(()())']
    # There's a few issues with the basic approach of splitting by '(' and ')'.
    # First, the ')' will be consumed and it will be impossible to tell
    # if a closing parentheses is part of the last group or not.
    # Second, the algorithm will break if we have unbalanced parentheses like
    # '((())'.
    # Idea:
    # It's much easier to keep track of how many '(' and ')' we have seen
    # as we iterate through the string.
    # We need a way to track whether we're inside a set of parentheses or not,
    # so we can add the ')' to the substring if we're not inside parentheses.
    # We also need a way to know when we start seeing a new set of parentheses
    # so we can add the opening '(' to the substring.
    # If we're inside parentheses, we don't want to add either the '(' or ')'
    # to the substring.
    # The solution is to have a stack that keeps track of the number of open
    # parentheses we've seen.
    # If we see an opening parentheses, we push onto the stack.
    # If we see a closing parentheses, we pop from the stack.
    # If the stack is empty, then we're not inside parentheses, and we can
    # add the ')' to the substring.
    # If the stack is not empty, then we're inside parentheses, and we don't
    # want to add either the '(' or ')' to the substring.
    # At the end of the iteration, we'll have a stack with the number of open
    # parentheses remaining in the groups. We can use that to know where to
    # split the string into separate groups.
    #
    # A few important things to keep in mind:
    # 1. Don't forget to pop from the stack when we start seeing a new set of parentheses.
    # 2. Don't forget to append the '(' to the substring when we start seeing a new set of parentheses.
    # 3. Don't forget to append the ')' to the substring when we stop seeing a new set of parentheses.
    # 4. Don't forget to
