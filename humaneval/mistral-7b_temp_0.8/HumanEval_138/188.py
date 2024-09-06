
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Test if the given number is even
    if n%2 != 0:
        return False

    # Test if the given number is the sum of exactly 4 positive even numbers
    for i in range(n//2):
        for j in range(n//2):
            for k in range(n//2):
                for l in range(n//2):
                    if i + j + k + l == n and i > 0 and j > 0 and k > 0 and l > 0:
                        return True

    # If the given number is not the sum of exactly 4 positive even numbers, return False
    return False
