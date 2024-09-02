
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # check if n is even
    if n % 2 != 0:
        return False

    # check if n is a multiple of 4
    if n % 4 == 0:
        return False

    # check if n can be written as the sum of 2^k \* 3^l for some k, l
    if not is_divisible_by_2_and_3(n):
        return False

    # check if n can be written as the sum of 2^k \* 2^l \* 3^t for some k, l, t
    if not is_divisible_by_2_and_3(n // 2):
        return False

    # check if n can be written as the sum of 2^k \* 3^l \* 2^t for some k, l, t
    if not is_divisible_by_2_and_3(n // 3):
        return False

    # check if n can be written as the sum of 2^k \* 2^l for some k, l
    if not is_divisible_by_2_and_3(n // 2):
        return False

    # check if n can be written as the sum of 2^k \* 3^l \* 2^t for some k, l, t
    if not is_divisible_by_2_and_3(n // 3):
        return False

    # check if n can be written as the sum of 2^k \* 2^l \* 3^t for some k, l, t
    if not is_divisible_by_2_and_3(n // 4):
        return False

    return True
