
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # for i in range(4):
    #     for j in range(4):
    #         for k in range(4):
    #             for l in range(4):
    #                 if i+j+k+l == n and i+j+k+l % 2 == 0:
    #                     return True
    # return False
    s = set()
    for i in range(2, n//2+1):
        s.add(n-i)
    return len(s.intersection(s)) == 4
