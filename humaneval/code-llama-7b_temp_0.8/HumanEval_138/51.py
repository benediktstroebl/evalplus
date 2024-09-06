
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even_numbers = [2, 4, 6, 8]
    for i in range(len(even_numbers)):
        for j in range(len(even_numbers)):
            for k in range(len(even_numbers)):
                for l in range(len(even_numbers)):
                    if even_numbers[i] + even_numbers[j] + even_numbers[k] + even_numbers[l] == n:
                        return True
    return False
