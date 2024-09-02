
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # The oddDigit function is written by your group.
    # You do not have to modify it.
    # return the product of all odd digits in the input integer n
    def oddDigit(n):
        count = 0
        while n:
            n = n/10
            count += 1
        return count
    def evenDigit(n):
        if n < 1:
            return 0
        elif n == 1:
            return 1
        else:
            return (n%10)/(n/10) + 1
    product = 1
    for i in range(1,n+1):
        product = product * oddDigit(i)
    return product
