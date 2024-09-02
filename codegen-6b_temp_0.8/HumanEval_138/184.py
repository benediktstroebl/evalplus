
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # your code here
    ssum = n
    s1pos = 0
    s2pos = 0
    while ssum > 0:
        s = ssum % 10
        ssum = ssum // 10
        if s % 2 == 0 and s > 0:
            s1pos += 1
        else:
            s2pos += 1
    if s1pos == 4 and s2pos == 4:
        return True
    else:
        return False

