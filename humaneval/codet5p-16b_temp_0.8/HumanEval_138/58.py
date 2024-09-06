
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n % 4!= 0 or n < 4:
        return False
    even_list = [2, 4, 6, 8]
    sum = 0
    while n > 0:
        for e in even_list:
            if n % e == 0:
                sum += e
                n = n / e
                break
    if sum == 4 * n:
        return True
    else:
        return False

