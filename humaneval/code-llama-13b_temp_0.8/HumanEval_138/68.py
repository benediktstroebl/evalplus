
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # Quadratic equation
    # even numbers: 2,4,6,8,10,12,14,16,18,20,22,24,26,28,30
    # odd numbers: 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29
    # sum of 4 even numbers is 4*n=4n
    # sum of 4 odd numbers is 4*n-4=4n-4
    if n%2==0:
        return True
    else:
        return False

