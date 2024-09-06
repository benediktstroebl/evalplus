
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        return n
    # modulo 10 gets the rightmost digit
    digit = n % 10
    # without the rightmost digit
    rest = n // 10
    # if the digit is even
    if digit % 2 == 0:
        # return the product of the rest of the digits
        return digits(rest)
    # otherwise, return the product of the rest with the current digit
    return rest * digit

