
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Base case
    if n <= 0:
        return False

    # Handle special case of 1
    if n == 1:
        return True

    # Handle special case of 2
    if n == 2:
        return True

    # Handle the remaining cases
    if n % 2 != 0:
        return False

    # Convert n to (2^n - 1) and check if it can be expressed as the sum of 4 even numbers
    # If not, return False
    num = 2**n - 1
    even_sum = sum(map(int, [2**i - 1 for i in range(n)]))

    if not is_equal_to_sum_even(even_sum):
        return False

    if not is_equal_to_sum_even(num / 2):
        return False

    if not is_equal_to_sum_even(num / 4):
        return False

    return True
