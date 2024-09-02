from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # TODO: write a loop to remove all the spaces from the given string
    # The loop has to remove all the spaces in the input string
    # the loop should not remove the characters from the string
    # you should not do this with a list comprehension
    # you can simply return the string after removing the spaces, which is the output of your loop
    input_string = paren_string.replace(" ", "")
    # TODO: write a loop that will traverse through the string
    # and open parentheses the loop has to count the number of open and close parentheses
    # the loop should return a list of the balanced sets of parentheses
    # each set will be represented by a string
    # you should not use a list comprehension
    # you can return the output of your loop which is a list of strings
    output = []
    for i in range(0, len(input_string)):
        if input_string[i] == '(':
            output.append(input_string[i])
        if input_string[i] == ')':
            output.append(input_string[i])
