

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
    matches = {")": "(", ">": "<", "<": ">"}
    queue = collections.deque()

    for i in range(len(brackets)):
        if brackets[i] == "<":
            queue.append(brackets[i])
        elif brackets[i] == ">":
            if queue:
                if queue[0] != matches[brackets[i]]:
                    return False
                else:
                    queue.popleft()
            else:
                return False
    return not queue

