
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # your code here
    s=str(num)
    l=[]
    for i in s:
        if int(i)%2==0:
            l.append(1)
        else:
            l.append(0)
    l=list(map(int,l))
    return tuple(l)
    pass
