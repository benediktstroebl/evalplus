
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # equal_to_sum = False
    # if n == 0:
    #     return True
    # if n % 2 == 0:
    #     equal_to_sum = True
    # if n % 2 != 0:
    #     equal_to_sum = False
    # if n > 0:
    #     for x in range(1,n):
    #         if x % 2 != 0:
    #             equal_to_sum = False
    #         if x % 2 == 0:
    #             equal_to_sum = True
    #             if x * 4 == n:
    #                 return True
    #         if x * 4 > n:
    #             equal_to_sum = False
    # return equal_to_sum
    return (n % 2 == 0) and (n > 0) and (1 + 2 + 3 + n / 2 == n)
