

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
    # correction of this bracketing is not in the scope of this course

    # main idea: find the index of the closing bracket for each opening bracket
    # then check that all brackets are closed

    # for clarity, we'll keep track of opening brackets and the brackets that they correspond to
    # i.e. the closing brackets
    open_brackets = []
    match_brackets = []

    for i in range(len(brackets)):
        if brackets[i] == '<':
            # if we find an opening bracket, we add a new element to our lists
            open_brackets.append(i)
            match_brackets.append(-1)
        elif brackets[i] == '>':
            # if we find a closing bracket, we check if there is a corresponding opening bracket
            if len(open_brackets) == 0:
                # there is none
                return False
            # if there is one, we get the index of the corresponding opening bracket
            # and store the index of the current closing bracket as the matching bracket of the opening one
            match_brackets[len(match_brackets) - 1] = i
            open_brackets.pop()

    if len(open_brackets) == 0:
        return True
    return False

