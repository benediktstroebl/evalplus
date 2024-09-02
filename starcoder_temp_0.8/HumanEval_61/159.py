

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    # We are going to use a stack.
    # push opening brackets on the stack
    # pop closing brackets
    # if there is more opening brackets than closing brackets, return False
    # return True when we have popped all opening brackets
    # We are not going to try to balance every bracket, just the ones that
    # are unbalanced and unmatched
    # open_count = 0
    # for b in brackets:
    #     if b == "(":
    #         open_count += 1
    #     elif b == ")":
    #         open_count -= 1
    #     if open_count < 0:
    #         return False
    # return open_count == 0

    # Use a queue instead of a stack
    # push opening brackets on the queue
    # pop closing brackets
    # if there is more opening brackets than closing brackets, return False
    # return True when we have popped all opening brackets
    # We are not going to try to balance every bracket, just the ones that
    # are unbalanced and unmatched
    # open_count = 0
    # for b in brackets:
    #     if b == "(":
    #         open_count += 1
    #     elif b == ")":
    #         open_count -= 1
    #     if open_count < 0:
    #         return False
    # return open_count == 0

    # If we are able to identify the first unmatched closing bracket,
    # we can use a second stack to detect unmatched opening brackets
    # before that closing bracket.
    # push opening brackets on the stack
    # if the next character is a closing bracket, pop it from the stack
    # if the next character is an opening bracket, push it on the stack
    # When the stack is empty, we have a valid string of balanced brackets
    # return True when we have popped all opening brackets
    # We are not going to try to balance every bracket, just the ones that
    # are unbalanced and unmatched
    # open_stack = []
    # for b in brackets:
    #     if b == "(":
    #         open_stack.append(b)
    #     elif b == ")":
    #         if open_stack == []:
    #             return False
    #         else:
    #             open_stack.pop()
    # return open_stack == []

    # There are no unmatched opening brackets
