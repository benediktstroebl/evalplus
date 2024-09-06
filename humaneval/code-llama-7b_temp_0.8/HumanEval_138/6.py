
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False

    arr = []
    i = 0
    while i < 3:
        arr.append(n - 2)
        n -= 2
        i += 1
    if n - sum(arr) == 0 or n - sum(arr) == 2:
        return True
    return False

