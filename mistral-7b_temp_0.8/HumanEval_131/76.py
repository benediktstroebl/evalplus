
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    #define a empty list to store odd digits
    odd_digits = []

    #split the integer into list of digits
    digits = [int(i) for i in str(n)]

    #iterate through the list of digits
    for digit in digits:
        #if digit is odd then append to the odd_digits list
        if digit % 2 != 0:
            odd_digits.append(digit)

    #if the length of the list is zero then return 0
    if len(odd_digits) == 0:
        return 0

    #if the length of the list is not zero then multiply all the elements in the list
    else:
        product = 1
        for num in odd_digits:
            product *= num
        return product

