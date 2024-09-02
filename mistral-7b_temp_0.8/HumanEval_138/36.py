
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 0:
        return False
    if n%2 != 0:
        return False
    even_number = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    total_even = 0
    for i in even_number:
        if i <= n:
            total_even += i
            if total_even > n:
                return False
        if total_even == n:
            return True
    return False
