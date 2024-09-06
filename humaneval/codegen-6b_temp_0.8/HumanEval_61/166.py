

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
    # if check(brackets):
    #     return True
    # else:
    #     return False
    #
    # from stack import Stack
    # s = Stack()
    #
    # for char in brackets:
    #     if char == ")":
    #         if s.is_empty() or s.top() != "(":
    #             return False
    #         else:
    #             s.pop()
    #
    #     else:
    #         s.push(char)
    #
    # return s.is_empty()


    # # Another process
    # # adding "(", ")", "(" to the end of the string
    # brackets = "(" + brackets + ")"
    #
    # # remove (
    # brackets = brackets.replace("(", "")
    # # remove )
    # brackets = brackets.replace(")", "")
    #
    # # test if there is any ) without a corresponding (
    # # otherwise, it is not balanced
    # if ")" not in brackets:
    #     return False
    #
    # # create a stack to store the left "("s
    # stack = Stack()
    #
    # for char in brackets:
    #     if char == "(":
    #         stack.push(char)
    #
    #     elif char == ")":
    #         if stack.is_empty():
    #             return False
    #         else:
    #             stack.pop()
    #
    # # check if the stack is empty
    # if stack.is_empty():
    #     return True
    # else:
    #     return False


    # method 2
    if brackets[0] != ")" or brackets[-1] != "(":
        return False

    counter = 0
    for i in range(len(brackets)):
        if brackets[i] == "(":
            counter += 1
        else:
            counter -= 1

        if counter < 0:
            return False

    return True

