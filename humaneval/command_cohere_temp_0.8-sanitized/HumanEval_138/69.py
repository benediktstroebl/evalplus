def is_equal_to_sum_even(n):
    # Check whether n can be written as the sum of 4 positive even numbers
    # First, set up equation as sum of two pairs
    even1, even2 = n // 2, n // 2
    # If both even numbers are positive (non-negative), return True
    return (even1 >= 0 and even2 >= 0 and even1 <= even2) or (even1 >= even2 and even2 == 0)