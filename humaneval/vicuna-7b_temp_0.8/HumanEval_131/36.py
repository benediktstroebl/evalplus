
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    # Check if any digit is odd
    for i in range(len(str(n))):
        if n % 10 == i % 2:
            continue
        # if the current digit is odd, return the product of the odd digits
        d = 1
        for j in range(i, len(str(n))):
            if n % 10 == j % 2:
                continue
            d *= 10
        return d

print(digits(1234567))