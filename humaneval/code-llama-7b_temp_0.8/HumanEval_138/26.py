
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n = int(n)
    even_sum = 0
    for i in range(1,n):
        if i % 2 == 0:
            even_sum += i
            if even_sum == n:
                return True
    return False

