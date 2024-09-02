

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    #initialize decreasing flag
    decreasing = False

    #check if list is increasing
    #if it isn't set decreasing flag
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            decreasing = True

    #if the list is increasing return True
    if decreasing == False:
        return True
    #else if the list is decreasing, return True
    elif decreasing == True:
        return True
    #else if neither is true, return False
    else:
        return False

