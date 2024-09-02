
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    a,b=min(a,b),max(a,b)
    l=[]
    for i in range(a, b+1):
        s=str(i)
        for i in s:
            if int(i)%2==0:
                l.append(int(i))
    return l
