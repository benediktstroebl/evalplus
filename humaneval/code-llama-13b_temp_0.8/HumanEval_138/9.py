
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 1:
        return False
    else:
        n = n / 2
        n1, n2, n3, n4 = 1, 2, 3, 4
        while n1 <= n:
            s = n1 + n2 + n3 + n4
            if s == n:
                return True
            if s > n:
                n4 += 2
                n3 += 2
                n2 += 2
                n1 += 2
                if n1 > n:
                    return False
            else:
                n4 += 2
                n3 += 2
                n2 += 2
                n1 += 2
        return False

