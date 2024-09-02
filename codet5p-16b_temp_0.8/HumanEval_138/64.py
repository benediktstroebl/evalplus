
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers_list = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            numbers_list.append(i)
    if len(numbers_list)!= 4:
        return False
    else:
        numbers_list.sort()
        return numbers_list[0] + numbers_list[1] == numbers_list[2] + numbers_list[3]

