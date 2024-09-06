def is_equal_to_sum_even(n):
    # Check whether n can be written as the sum of 4 positive even numbers
    # Calculate n in binary
    binary_n = bin(n)[2:]
    if '1' in binary_n or '0' in binary_n.rstrip('0'):
        return False
    return True