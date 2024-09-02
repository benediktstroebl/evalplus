
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n_as_array = []
    n_as_array[:0] = n
    sums = []
    for i in range(len(n_as_array)):
        for j in range(len(n_as_array)):
            if i == j:
                pass
            else:
                if n_as_array[i] + n_as_array[j] == n:
                    sums.append(n_as_array[i])
                    sums.append(n_as_array[j])
    return len(sums) == 4

