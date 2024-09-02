
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check if all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    # check if n has an odd digit
    if n % 2 != 0:
        # find the index of the first odd digit
        i = bisect_left(str(n), str.isdigit)
        # compute the product of the odd digits
        prod = 1
        for j in str(n)[i:]:
            if j.isdigit() and j % 2 != 0:
                prod *= int(j)
        return prod

a = int(input("Enter an integer: "))
n = digits(a)
