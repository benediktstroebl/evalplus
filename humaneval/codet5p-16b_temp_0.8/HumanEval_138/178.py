
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n_str = str(n)
    n_str_sorted = "".join(sorted(n_str))
    
    sums = 0
    for i in range(1, 5):
        sums += int(n_str_sorted[i-1])
    
    return sums % 2 == 0
    
