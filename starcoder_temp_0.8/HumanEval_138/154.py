
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    numbers = [x for x in range(1, n + 1) if x % 2 == 0]
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                for l in range(k + 1, len(numbers)):
                    if numbers[i] + numbers[j] + numbers[k] + numbers[l] == n:
                        return True
    return False

