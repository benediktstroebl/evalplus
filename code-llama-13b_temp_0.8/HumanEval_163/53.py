
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # make sure a and b are both positive integers
    assert a > 0 and b > 0, 'Arguments must be positive integers'

    # make sure a <= b
    if a > b:
        a, b = b, a

    # we'll use range to iterate over a range of integers
    # this range will start with a, and go to b+1
    # (since range(a, b) does not include b)
    my_range = range(a, b+1)

    # an empty list we can start adding even numbers to
    even_numbers = []

    # iterate over the range
    for n in my_range:

        # modulo: %
        # this gives us the remainder of n / 2
        # if this remainder is zero, n is even
        if n % 2 == 0:
            even_numbers.append(n)

    return even_numbers

