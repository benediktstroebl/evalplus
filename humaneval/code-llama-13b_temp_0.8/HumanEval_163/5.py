
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Convert arguments to strings and remove first digit if it is '1'
    a = str(a)[1:] if str(a)[0] == '1' else str(a)
    b = str(b)[1:] if str(b)[0] == '1' else str(b)

    # Pad strings with zeros to make them have the same length
    len_a, len_b = len(a), len(b)
    a = ('0' * (len_b - len_a)) + a if len_a < len_b else a
    b = ('0' * (len_a - len_b)) + b if len_a > len_b else b

    # Reverse strings
    a, b = a[::-1], b[::-1]

    # Find the position where the integers start to differ.
    # This is when they start to have different digits or the end of the
    # shorter string is reached
    for i, (c, d) in enumerate(zip(a, b)):
        if c != d:
            break

    # Create a list of integers from the last common digit to the end of the
    # shorter string, reversed
    r = list(map(int, a[:i][::-1] + '0123456789'))

    # If there is a carry over from the left of the shorter string, add it
    # to the end of the list
    if i < len_b:
        r.append(int(b[i]))

    # Return the even digits of the resulting integer, in ascending order
    return sorted([int(d) for d in str(sum(r)) if int(d) % 2 == 0])
