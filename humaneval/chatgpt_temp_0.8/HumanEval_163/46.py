def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # initialize an empty list to store the even digits
    even_digits = []

    # loop through the range from a to b inclusive
    for num in range(a, b+1):

        # loop through the digits in the current number
        for digit in str(num):

            # if the digit is even, append it to the even_digits list
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # sort the even digits list in ascending order
    even_digits.sort()

    # remove duplicates from the even digits list
    even_digits = list(set(even_digits))

    return even_digits
