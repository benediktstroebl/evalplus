
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    num = []
    for i in range(4):
        if 4*i + 1 <= n:
            num.append(4*i + 1)
        elif 4*(i+1) - 1 <= n:
            num.append(4*(i+1) - 1)
    if n in num:
        return False
    elif sum(num) != n:
        return False
    else:
        return True

