
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # SOLUTION
    #   Convert to strings.
    #   Find the right length.
    #   Iterate through the right length.
    #   Check if the string is an integer.
    #   If not, discard.
    #   Otherwise, add it to the list.
    #   Sort the list.
    #   Convert back to integers.
    l = [str(x) for x in range(a, b + 1)]
    max_len = max([len(x) for x in l])
    result = []
    for s in l:
        if len(s)!= max_len:
            continue
        if not s.isdigit():
            continue
        result.append(int(s))
    return sorted(result)
