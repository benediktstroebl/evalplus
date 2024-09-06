
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # convert the input integers to strings
    a = str(a)
    b = str(b)

    # create a list to store the even digits
    digits = []

    # loop through the digits, starting from the right
    for i in range(len(b) - len(a)):
        # append the leftmost digit of the first number to the list
        digits.append(a[0])

        # add the next digit of the first number to the list
        digits.append(a[1])

        # subtract the second number from the first number
        a = str(int(a[1]) - b[0])

        # remove the second number from the list
        digits.remove(b[0])

        # remove the first number from the list
        digits.remove(a[0])

        # loop through the digits, starting from the right
        for j in range(len(b) - len(a)):
            # subtract the next digit of the first number from the second number
            b = str(int(b[1]) - a[1])

            # remove the next digit of the first number from the list
            digits.remove(a[1])

            # remove the first number from the list
            digits.remove(b[1])

            # add the next digit of the first number to the list
            digits.append(a[1])

    # return the even digits in ascending order
    return digits