
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
    # your code here
    r=[]
    for n in x:
        r.append([i for i in str(n) if i.isdigit()])
    for i in r:
        if len(set(i))==len(i):
            if int(''.join(i))%2==0:
                continue
            else:
                print(int(''.join(i)))
                return int(''.join(i))
