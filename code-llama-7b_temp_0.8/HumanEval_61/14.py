

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

    # how can you tell if the brackets are balanced?
    # 1. every opening bracket has a corresponding closing bracket

    # the number of open brackets is equal to the number of close brackets
    # can I count the number of open brackets and the number of close brackets?
    # can I make a function to count open brackets in a string?

    def count_open(string):
        count = 0
        for char in string:
            if char == '(':
                count += 1
        return count

    def count_close(string):
        count = 0
        for char in string:
            if char == ')':
                count += 1
        return count

    if count_open(brackets) == count_close(brackets):
        return True
    else:
        return False


