
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Example of using a recursive approach
    def digits_rec(n, acc=0):
        if n == 0:
            return acc
        if n % 2 == 0:
            return acc * 10 + (n // 2)
        return acc * 10 + n + 1

    # Example of using an iterative approach
    acc = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            acc = acc * 10 + i
        else:
            acc = acc * 10 + i + 1
    return acc
