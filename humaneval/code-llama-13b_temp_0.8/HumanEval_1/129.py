from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # NOTE: this problem is impossible to solve without using stacks.
    #       Think about it: what do you do when you encounter the opening brace of a nested group?
    #       You can't just put it into the string you're building, since it might be a part of some other group
    #       as well. So you need to put it aside, and then, when the nested group is over, bring it back.
    #       Exactly the kind of thing stacks are made for!
    #
    # Hint: when you encounter an open brace, push it into the stack.
    #       When you encounter a close brace, pop the top element from the stack, append it to the current group
    #       and repeat the process with the rest of the string.
    #       When the stack becomes empty, the current group is complete.
    #       When there's nothing left in the string, return the list of groups
    #
    # Hint 2: Since the groups are not nested within each other, you can solve this problem in one pass.
    #         Look at each character in the string one by one, without looking at the rest of the string.
    #
    # Hint 3: The loop below goes through the string character by character.
    #         You can use the "for char in paren_string" syntax to get the current character in the string
    #         inside the loop.
    ...

    # Solution 1:
    # return []  # Put your solution here

    # Solution 2:
    # return []  # Put your solution here

