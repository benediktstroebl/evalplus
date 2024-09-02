
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return []
    else:
        a_idx = bisect.bisect_right(str(a), '0')
        b_idx = bisect.bisect_left(str(b), '0')
        if a_idx == b_idx:
            return [str(a)[a_idx+1:]]
        else:
            return [str(a)[a_idx+1:], str(b)[b_idx+1:]]
            
