
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even = [x for x in range(2,n+1) if x % 2 == 0]
    for i in even:
        for j in even:
            for k in even:
                if (i + j + k + n) == n:
                    return True
    return False
