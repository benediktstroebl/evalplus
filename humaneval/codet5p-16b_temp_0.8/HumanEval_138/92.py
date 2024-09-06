
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n%2!= 0:
        return False
    n_even = n/2
    n_even_str = str(n_even)
    even_sum = 0
    for i in n_even_str:
        even_sum += int(i)
    return even_sum == 4
