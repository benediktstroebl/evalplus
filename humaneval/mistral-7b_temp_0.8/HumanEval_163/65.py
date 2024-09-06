
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Your code here
    # int_list = [x for x in range(a,b+1) if len(str(x))%2 ==0]
    # return sorted(int_list)
    return sorted([int(x) for x in list(filter(lambda n:len(str(n))%2==0,range(a,b+1)))])
