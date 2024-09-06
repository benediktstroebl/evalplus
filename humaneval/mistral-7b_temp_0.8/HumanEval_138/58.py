
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    lst = [i for i in range(0, n + 1)]
    sum_list = []
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            sum_list.append(lst[i] + lst[j])
    return sum_list
