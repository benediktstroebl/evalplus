
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # split input range into two parts
    a_, b_ = [int(i) for i in input("Enter a positive integer: ").split()]
    
    # store even digits in a list
    digits = []
    
    # iterate over the range
    for i in range(a_, b_):
        digits.append(i % 2)
    
    # return the list of even digits
    return digits
