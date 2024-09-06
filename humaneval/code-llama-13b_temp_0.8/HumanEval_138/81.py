
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even_numbers = []
    if n % 2 != 0:
        return False
    for i in range(2, (n // 2) + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    for i in range(len(even_numbers)):
        for j in range(i, len(even_numbers)):
            for k in range(j, len(even_numbers)):
                for l in range(k, len(even_numbers)):
                    if even_numbers[i] + even_numbers[j] + even_numbers[k] + even_numbers[l] == n:
                        return True
    return False
