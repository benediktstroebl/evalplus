
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # 440089534392
    # 440089534392%10 == 2
    # 440089534392//10 == 44008953439
    # 44008953439%10 == 9
    # 44008953439//10 == 4400895343
    # 4400895343%10 == 3
    # 4400895343//10 == 440089534
    # 440089534%10 == 4
    # 440089534//10 == 44008953
    # 44008953%10 == 3
    # 44008953//10 == 4400895
