
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Method 1, Brute force
    # return (n % 2 == 0) and (n % 4 == 0) and sum([x for x in range(1, int(n / 2) + 1) if n % (2 * x) == 0]) == n

    # Method 2, idea from https://www.quora.com/Can-you-factor-4020-using-4-positive-even-numbers
    # x = 1
    # while n > x:
    #     if n % (2 * x) == 0:
    #         return True
    #     x += 1
    # return False

    # Method 3, idea from https://www.quora.com/Can-you-factor-4020-using-4-positive-even-numbers
    i = 1
    while i < n:
        if n % (2 * i) == 0:
            return True
        i += 1
    return False

