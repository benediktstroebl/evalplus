

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
    # Your code here
    queue = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            queue.append(i)
        elif brackets[i] == ">":
            if queue:
                queue.pop()
            else:
                return False
    return queue == []
