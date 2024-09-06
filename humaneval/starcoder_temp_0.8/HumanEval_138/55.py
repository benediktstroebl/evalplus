
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    num_list = []
    for i in range(4):
        if n - i < 2 or n - i % 2 == 1:
            return False
        num_list.append(n - i)
    return sum(num_list) == n

