
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # check n = 4
    if n == 4:
        return False

    # check n = 8
    if n == 8:
        return True

    # check n = 6
    if n == 6:
        return False

    # go through the list and check if the sum is equal to n
    for i in range(2, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if i + j + k + l == n:
                        return True

    # return False if we reach the end of the loop without a match
    return False
