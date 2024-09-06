
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Add a space to the end of your string to simplify testing.
    # Please use the built-in function int() to convert the string
    # digits into integers. Do not convert them to integers
    # individually!
    s1 = str(a)
    s2 = str(b)

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    s1 = s1.rstrip("0")
    s2 = s2.rstrip("0")

    start = 0
    if s1:
        start = int(s1[-1])
    end = 0
    if s2:
        end = int(s2[-1])

    result = []
    for i in range(start, end + 1, 2):
        result.append(str(i))

    return result
