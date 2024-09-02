
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n = str(n)

    # Check whether the given number is even
    if n[0] == '0' or n[1] == '0':
        return False
    if int(n) % 2 != 0:
        return False

    # Check whether the given number is a sum of 4 even numbers
    for i in range(5, int(n)+1, 2):
        if n[-i:] == n[-2*i:-i]:
            return True
    return False

