

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
    # # An opening bracket at index i is matched with a closing
    # # bracket at index j if j is less than the length of the string
    # # and the character at index j is the matching closing bracket
    # # for the character at index i.
    # for i in range(len(brackets)):
    #     if brackets[i] == "<":
    #         for j in range(len(brackets)):
    #             if brackets[j] == ">":
    #                 if i < j:
    #                     if not brackets[i:j].count("<") == brackets[i:j].count(">"):
    #                         return False
    #     else:
    #         return False
    # return True
    # An opening bracket at index i is matched with a closing
    # bracket at index j if j is less than the length of the string
    # and the character at index j is the matching closing bracket
    # for the character at index i.
    for i in range(len(brackets)):
        if brackets[i] == "<":
            opening = i
            while opening > 0:
                opening = brackets.find("<", opening + 1)
                if opening == -1:
                    return False
                if brackets[opening + 1] == ">":
                    return True
        else:
            return False
    return True
