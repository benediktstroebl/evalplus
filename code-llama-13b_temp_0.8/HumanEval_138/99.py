
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2 != 0:
        return False
    a = n/4
    for b in range(1,a+1):
        for c in range(1,a+1):
            for d in range(1,a+1):
                if b!=c and b!=d and c!=d:
                    if (b+c+d+a) == n:
                        return True
    return False
