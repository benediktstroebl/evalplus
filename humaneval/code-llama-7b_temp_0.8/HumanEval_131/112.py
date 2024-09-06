
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # your code here
    # converting to string to make odd number of digits
    n = str(n)
    # joining all the digits
    n = ''.join(n)
    # converting to int to make it a number
    n = int(n)
    # a flag to check for even or odd digits
    flag = False
    prod = 1
    # checking for odd digits
    while(n != 0):
        # extracting last digit
        ld = n % 10
        # making the last digit to be even
        if(ld % 2 == 1):
            flag = True
        else:
            # skipping the even digits
            n //= 10
            continue
        # multiplying all the odd digits
        prod = prod * ld
        # multiplying with last digit
        n //= 10
    # returning the product or 0
    return prod if flag else 0

