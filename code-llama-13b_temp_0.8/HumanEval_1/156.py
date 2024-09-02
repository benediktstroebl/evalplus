from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT1: if you think of the problem as "separating words by spaces", then you can use the same algorithm
    #        to solve it that you use to split a sentence by spaces.
    # HINT2: implement a simple stack-based solution.
    # HINT3: to implement a simple stack-based solution, you need to know 3 things:
    #        * how to check if the current char is an open brace
    #        * how to check if the current char is a closed brace
    #        * how to check if the stack is empty
    #        hint on how to do all that: ord(character)
    #        HINT4: to solve the balancing problem, use a counter. When you encounter an open brace,
    #        increase the counter. When you encounter a closed brace, decrease the counter.
    #        HINT5: to separate the groups, you need to know when the counter is back to 0.
    #        HINT6: if you do not know what ord() is, look it up on the web.
    raise NotImplementedError
