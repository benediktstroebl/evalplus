from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT1: You can use a stack to keep track of parentheses and count the balance
    # HINT2: Make sure not to forget empty groups
    # HINT3: To check if a group is empty you can check if the first element is closing
    # HINT4: If you are interested, you can look up 'Shunting-yard algorithm'
    # HINT5: Make sure to clean the input before processing
    # HINT6: Use a stack to keep track of the groups you've found so far
    # HINT7: After processing the whole string, you should have a list of balanced groups.
    #        Note that this will not check for the correct balance of the parentheses
    result: List[str] = []
    stack = []
    for i in paren_string.replace(" ", ""):
        if i in "(":
            stack.append(i)
        elif i in ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
                result.append(i)
            else:
                stack.append(i)
        else:
            raise ValueError("paren_string should only contain parentheses")
    return result

