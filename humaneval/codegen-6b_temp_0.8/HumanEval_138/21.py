
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # if n is negative
    if n < 0:
        return False
    # Edge case
    if n == 0:
        return True
    # if there is not even number, return false
    if n % 2 != 0:
        return False
    # Step 1: split the number into chunks of 4
    chunk_nums = [n - i * 4 for i in range(4)]
    # Step 2: if any of the chunk is less than 0, the number is not equal to the sum of 4 even numbers
    for chunk in chunk_nums:
        if chunk < 0:
            return False
    # otherwise the number is equal to the sum of 4 even numbers
    return True
