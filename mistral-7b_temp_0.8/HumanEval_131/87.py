
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # the idea here is to break up the number into an array of digits and
    # then use a filter to eliminate any even numbers in the list and then
    # multiply the remaining numbers.
    #
    # eg.
    #   digits(12345)
    #   digits([1,2,3,4,5])
    #   digits([1,3,5])
    #   digits([5])
    #   digits(5)
    #   digits(0)
    #
    # As we need to return a single number, rather than a list, the
    # answer will be the product of the digits
    #
    # eg.
    #   digits([1,3,5])
    #   digits([1,3,5])
    #   digits([1,3,5])
    #   digits(5)
    #   digits(0)
    #   digits(5)
    #
    # as there are no even numbers, we return the product of the digits.
    #
    
