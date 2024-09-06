
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    list_of_numbers = []
    for i in range(2, n):
        if i % 2 == 0:
            list_of_numbers.append(i)

    if len(list_of_numbers)!= 4:
        return False

    sum_of_list = sum(list_of_numbers)
    if sum_of_list == n:
        return True
    else:
        return False

