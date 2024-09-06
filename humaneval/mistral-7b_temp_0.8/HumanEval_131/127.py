
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # your code here

    product = 1
    #print(n)
    for num in str(n):
        #print(num)
        #print(num, isEven(num))
        if not isEven(num):
            product *= int(num)
        else:
            product = 0
    return product
