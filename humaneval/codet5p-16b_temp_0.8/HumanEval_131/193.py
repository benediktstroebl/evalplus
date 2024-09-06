
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits_list = [int(x) for x in str(n)]
    for number in digits_list:
        if number%2 == 0:
            return 0
    return 0 if all(x%2 == 0 for x in digits_list) else 1
    
