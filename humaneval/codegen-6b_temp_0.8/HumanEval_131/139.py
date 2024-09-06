
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def digits_helper(n):
        if n < 10:
            return n
        else:
            return n % 10 * digits_helper(n // 10)


    num_str = str(n)
    return sum(map(int, list(num_str))) * 1 if len(num_str) % 2 == 0 else digits_helper(n)
