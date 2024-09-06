
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # 1st way
    # for a in range(1, n):
    #     for b in range(a, n):
    #         for c in range(b, n):
    #             for d in range(c, n):
    #                 if (a + b + c + d == n) and (a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0):
    #                     return True
    # return False

    # 2nd way
    # for a in range(1, n):
    #     if (n - a) % 2 == 0:
    #         if (n - a) / 2 >= a:
    #             for b in range(a, int((n - a) / 2)):
    #                 if (n - a - b) % 2 == 0:
    #                     if (n - a - b) / 2 >= b:
    #                         for c in range(b, int((n - a - b) / 2)):
    #                             if (n - a - b - c) % 2 == 0:
    #                                 if (n - a - b - c) / 2 >= c:
    #                                     for d in range(c, int((n - a - b - c) / 2)):
    #                                         if (n - a - b - c - d) == 0:
    #                                             return True
    # return False

    # 3rd way
    # for a in range(1, n):
    #     if (n - a) % 2 == 0:
    #         b = (n - a) / 2
    #         if a <= b:
    #             if a % 2 == 0 and b % 2 == 0:
    #                 for c in range(a + 1, b, 2):
    #                     if (n - a - c) % 2 == 0:
    #                         d = (n - a - c) / 2
    #                         if c <= d:
    #                
