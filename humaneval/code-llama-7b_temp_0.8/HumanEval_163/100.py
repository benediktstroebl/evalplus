
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Only use two digits to calculate 
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Get the number of digits
    a_digits = get_number_of_digits(a)
    b_digits = get_number_of_digits(b)

    # Change a and b to one digit 
    # in order to make it easier to operate
    a = a % (10 ** (a_digits - 1))
    b = b % (10 ** (b_digits - 1))

    # Fill 0 to make a and b the same number
    # of digits
    if a_digits > b_digits:
        b = b * (10 ** (a_digits - b_digits))
    if b_digits > a_digits:
        a = a * (10 ** (b_digits - a_digits))

    # Now a and b should have the same number of digits
    # Try every digit, if the digit is even, check whether it
    # should be added to the result
    a_str = str(a)
    b_str = str(b)
    ans = []
    for i in range(a_digits):
        if int(a_str[i]) % 2 == 0:
            if int(a_str[i]) <= int(b_str[i]):
                ans.append(int(a_str[i]))
            else:
                ans.append(int(b_str[i]))

    return ans
