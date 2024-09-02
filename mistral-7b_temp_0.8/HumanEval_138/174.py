
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    a = list(range(2,n))
    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
    if sum(even) == n:
        return True
    else:
        return False
