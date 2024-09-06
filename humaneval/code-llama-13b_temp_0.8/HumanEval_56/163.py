

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
    # for i in range(len(brackets)):
    #     if brackets[i] == '<':
    #         n = 1
    #         for j in range(i, len(brackets)):
    #             if brackets[j] == '>':
    #                 n -= 1
    #                 if n == 0:
    #                     return correct_bracketing(brackets[j + 1:])
    #             elif brackets[j] == '<':
    #                 n += 1
    #     if n == 0:
    #         return correct_bracketing(brackets[i + 1:])
    # return False

    # for i in range(len(brackets)):
    #     if brackets[i] == '<':
    #         if i == len(brackets) - 1:
    #             return False
    #         if brackets[i + 1] == '>':
    #             return correct_bracketing(brackets[i + 2:])
    #         else:
    #             return False
    # return True

    # total = 0
    # for b in brackets:
    #     if b == '<':
    #         total += 1
    #     else:
    #         total -= 1
    # return total == 0

    return sum(brackets.count('<') - brackets.count('>') > 0) == 0

