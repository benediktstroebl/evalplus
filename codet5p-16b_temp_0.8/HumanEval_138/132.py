
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n_str = str(n)
    n_list = list(map(int, n_str))
    if sum(n_list) % 2!= 0:
        return False
    else:
        for i in range(len(n_list)):
            for j in range(i, len(n_list)):
                for k in range(j, len(n_list)):
                    for l in range(k, len(n_list)):
                        if i == j and j == k and k == l:
                            continue
                        elif n_list[i] + n_list[j] + n_list[k] + n_list[l] == sum(n_list):
                            return True
    return False
