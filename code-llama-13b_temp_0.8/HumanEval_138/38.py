
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # assert n > 0, 'n is less than 0'
    # result = False
    # even_counter = 0
    # for i in range(1, n + 1):
    #     if i % 2 == 0:
    #         even_counter += 1
    # if even_counter == 4:
    #     result = True
    # return result
    return (n % 4 == 0) and (n > 0)

