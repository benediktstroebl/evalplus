
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    eve = 0
    odd = 0
    i = 2
    while i <= n:
        if i % 2 == 0:
            eve += i
        else:
            odd += i
        i += 1
    return (eve == n)





