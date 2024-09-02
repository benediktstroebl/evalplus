
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    from collections import Counter
    from itertools import combinations
    if n % 2 != 0 or n < 4:
        return False
    c = Counter([2**i for i in range(1,int(n**.5)+1)])
    return sum(c.values()) == 4 and len(c) == 4
