

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # use a stack to keep track of the index of '<' we have seen so far
    stack = []
    # we can use this loop to iterate through the characters in brackets
    for index, bracket in enumerate(brackets):
        if bracket == '<':
            # 'push' the index of the '>' we've seen
            stack.append(index)
        elif bracket == '>':
            # check if stack is empty
            if not stack:
                return False
            else:
                # if not empty, pop the index of the last '<' we've seen
                last_open_bracket_index = stack.pop()
                # check if the closing bracket matches the last open bracket
                if last_open_bracket_index != index - 1:
                    return False
    return len(stack) == 0
