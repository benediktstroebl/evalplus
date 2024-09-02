
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    n=b
    r=[]
    while n>a:
        r.append(n%10)
        n=n//10
    r.reverse()
    if r[0]%2==0:
        return r
    else:
        return generate_integers(a,b+1)
