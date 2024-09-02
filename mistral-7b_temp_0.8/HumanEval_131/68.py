
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def helper(num):
        if num <= 0:
            return 0
        else:
            if num%2 == 0:
                return 0
            else:
                return helper(num/10) + num%10
    return helper(n)
