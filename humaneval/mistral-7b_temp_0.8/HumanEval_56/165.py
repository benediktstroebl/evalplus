

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
    brackets = list(brackets)
    # Create a list that keeps track of the opening brackets and their corresponding closing brackets
    opening_brackets = []
    opening_brackets_index = []
    closing_brackets = []
    closing_brackets_index = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            opening_brackets.append("<")
            opening_brackets_index.append(i)
        elif brackets[i] == ">":
            closing_brackets.append(">")
            closing_brackets_index.append(i)

    # Check if all opening brackets have a corresponding closing bracket
    for opening_bracket in opening_brackets:
        if opening_bracket not in closing_brackets:
            return False

    # Check if all closing brackets have a corresponding opening bracket
    for closing_bracket in closing_brackets:
        if closing_bracket not in opening_brackets
