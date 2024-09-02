
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = str(n)
    if n[0] == '-': return False
    s = 0
    for c in n:
        s += int(c)
    return s % 4 == 0 and s//4 in [2,3,4]
