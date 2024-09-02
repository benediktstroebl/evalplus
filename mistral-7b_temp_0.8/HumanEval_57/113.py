

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Write your code here.
    if len(l)==0:
        return True
    elif len(l)==1:
        return True
    else:
        if l[0]>l[1]:
            for i in range(0,len(l)-1):
                if l[i+1]<l[i]:
                    return False
        elif l[0]<l[1]:
            for i in range(0,len(l)-1):
                if l[i+1]>l[i]:
                    return False

        return True
