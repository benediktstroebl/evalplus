
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check if all digits are even
    if sum(map(int, str(n))) % 2 == 0:
        return 0
    
    # compute the sum of all digits
    digits = [int(d) for d in str(n)]
    odd_digits = [d for d in digits if d % 2 != 0]
    sum_of_odd = sum(odd_digits)
    
    # if there are no odd digits, return 0
    if not odd_digits:
        return 0
    
    # compute the product of the odd digits
    return sum_of_odd * (len(odd_digits) - 1) // 2
