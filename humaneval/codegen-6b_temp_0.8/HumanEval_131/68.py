
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # the following solution requires O(n) space;
    # solutions that do not use an additional array other than a
    # string will require O(n) space (which is O(D) space since we
    # need to create a new array of length n to contain the digits)
    # the \s is a whitespace character; we do not want to preserve it
    # in the resulting digit product

    # the division operator / divides the first operand by the second
    # and returns a floating point value; here we are dividing by #'s
    digit_product = float(n % 10)/1

    # k is the remainder of n divided by 10; here k=0
    # the modulo operator % yields the remainder of a division
    # operation with the first operand and the second operand.
    # the second operand is subtracted from the first
    # and the result is stored in k; here k=(n/10)
    while n > 9:
        n = n/10
        digit_product = digit_product * (int(n % 10)/1)

    if digit_product == 0:
        # the number is all even, so the result is 0
        return 0
    else:
        # the result is not all even, so the first digit product is
        # x, and the second is y to get the product of odd digits
        # x*y = the product of odd digits in the number
        return digit_product

