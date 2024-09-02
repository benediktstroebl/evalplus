
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # your code here
    count = 0
    i = 2
    while count < 4:
        if n == i:
            return True
        elif n > i:
            n = n - i
            count = count + 1
        elif n < i:
            i = i + 2
    return False
