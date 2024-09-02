
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # If all digits are even, return 0
    if all(d % 2 == 0 for d in n):
        return 0
    
    # Calculate the sum of the digits and reverse the number
    num, denom = map(int, n.split('.')), 1
    while denom:
        num, denom = denom, num // 10
    
    # Calculate the product of the odd digits
    odd_digits = [d % 2 for d in str(num)]
    return sum(odd_digits)
