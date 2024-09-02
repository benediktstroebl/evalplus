
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    n=0
    for i in arr:
        c=0
        if i<0:
            n+=1
        else:
            while i>0:
                d=i%10
                i//=10
                c+=d
            if c>0:
                n+=1
    return n
