
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n = int(n)
    sum = 0
    for i in range(2, 100):
        if n - i < 0:
            break
        if n % i == 0:
            sum += i
    if sum != n:
        return False
    else:
        return True

