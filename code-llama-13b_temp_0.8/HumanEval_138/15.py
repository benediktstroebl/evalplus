
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # Split number in pairs of two digits
    digits = split_digits(n)
    # For each pair of two digits
    for i in range(0, len(digits), 2):
        # Check that the pair is an even number
        if not is_even(int(digits[i] + digits[i + 1])):
            return False

    # Sum the digits and check that it is even
    return is_even(sum([int(i) for i in digits]))

