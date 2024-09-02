
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return False
    if n < 4:
        return False
    n_list = []
    for i in range(2, n//2):
        if n % i == 0:
            n_list.append(i)
    if len(n_list) != 4:
        return False
    else:
        return all(x % 2 == 0 for x in n_list)
    