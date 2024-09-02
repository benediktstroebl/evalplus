

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    """
    Set last number as max/min val
    Count number of times number changes
    Check if number of times number changes is 2 or more
    """
    increasing = None
    decreasing = None
    num_of_changes = 0

    if len(l) == 0:
        return False

    last_num = l[-1]
    l.pop()

    for i in l:
        if i == last_num:
            num_of_changes += 1

        if i < last_num:
            if not increasing:
                increasing = i
            else:
                increasing = False
                decreasing = last_num
                break
        elif increasing and i > increasing:
            increasing = i
        else:
            decreasing = i
    
    return increasing != None and increasing == increasing


