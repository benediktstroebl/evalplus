
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    #your code goes here
    unique = set()
    for i in x:
        temp = 0
        while i:
            temp = temp*10 + i%10
            if temp%2==0:
                break
            i=i//10
        else:
            unique.add(temp)
    return sorted(unique)
