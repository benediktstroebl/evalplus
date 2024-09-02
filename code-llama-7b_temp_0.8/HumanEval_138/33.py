
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even_nums = [2,4,6,8]
    for num in even_nums:
        for num_2 in even_nums:
            for num_3 in even_nums:
                for num_4 in even_nums:
                    if(num+num_2+num_3+num_4==n):
                        return True
    return False

