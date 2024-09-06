
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 10 and n % 2 == 0:
        return True
    for a in range(2,n+1):
        if a % 2 == 0:
            for b in range(a,n+1):
                if b % 2 == 0:
                    for c in range(b,n+1):
                        if c % 2 == 0:
                            for d in range(c,n+1):
                                if d % 2 == 0:
                                    if a+b+c+d == n:
                                        return True
    return False

