
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # original idea from https://www.hackerrank.com/challenges/ctci-array-left-rotation/forum/comments/2147175
    # no idea how to rotate an array with the slight variation that this gives the same answer with less code
    # and the accepted solution is better
    # no idea how to return this solution
    return sum(lst[i] for i in range(len(lst)/2) if ((i + 1) % 2) == 0) * lst[0]

