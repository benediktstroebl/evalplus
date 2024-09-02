
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2 != 0:
        return False
    even_count = 0
    for n in range(2,n):
        if n%2 != 0:
            even_count += 1
            if even_count >= 4:
                return False
        if even_count == 4 and n == n:
            return True
