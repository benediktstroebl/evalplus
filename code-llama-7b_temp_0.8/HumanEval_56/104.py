

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
    "*** YOUR CODE HERE ***"
    #Without recursion
    # while "<" in brackets:
    #     if brackets.count("<") > brackets.count(">"):
    #         return False
    #     else:
    #         if brackets.count("<") == brackets.count(">"):
    #             return True
    #     brackets = brackets.replace("<", "", 1)
    #     brackets = brackets.replace(">", "", 1)

    #With recursion
    # if brackets.count("<") > brackets.count(">"):
    #     return False
    # if brackets.count("<") == brackets.count(">"):
    #     return True
    # else:
    #     return correct_bracketing(brackets.replace("<", "", 1))

    #Find the index of < in brackets
    # if "<" in brackets:
    #     if brackets.index("<") < brackets.index(">"):
    #         return correct_bracketing(brackets.replace("<", "", 1))
    #     else:
    #         return False
    # else:
    #     return True

    #Without recursion
    # return "<" not in brackets or correct_bracketing(brackets.replace("<", "", 1))

    #With recursion
    # if "<" in brackets:
    #     return correct_bracketing(brackets.replace("<", "", 1))
    # else:
    #     return ">" not in brackets or correct_bracketing(brackets.replace(">", "", 1))

    #With while loop
    # while "<" in brackets:
    #     if brackets.index("<") < brackets.index(">"):
    #         return correct_bracketing(brackets.replace("<", "", 1))
    #     else:
    #         return False
    # else:
    #     return ">" not in brackets

    #With for loop
    # for i in range(len(brackets)):
    #     if brackets[i] == "<":
    #         if i < len(brackets) - 1:
    #             if brackets[i+1] == ">":
    
