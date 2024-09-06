
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 4 or n % 2 != 0:
        return False
    evens = [i for i in range(2, n + 1) if i % 2 == 0]
    for i in range(0, len(evens) - 3):
        for j in range(i + 1, len(evens) - 2):
            for k in range(j + 1, len(evens) - 1):
                for l in range(k + 1, len(evens)):
                    if evens[i] + evens[j] + evens[k] + evens[l] == n:
                        return True
    return False
