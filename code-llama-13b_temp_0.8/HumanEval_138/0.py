
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check that n is greater than 0
    if n > 0:
        # Check that n is even
        if n % 2 == 0:
            # Check that n is even
            for x in range(1, (n // 2) + 1):
                # Check that x is even
                if x % 2 == 0:
                    # Check that n - x is even
                    if (n - x) % 2 == 0:
                        # Check that n - x is greater than 0
                        if (n - x) > 0:
                            # Check that (n - x) / 2 is greater than 0
                            if (n - x) // 2 > 0:
                                # Check that (n - x) / 2 is even
                                if ((n - x) // 2) % 2 == 0:
                                    # Check that n - (n - x) / 2 is greater than 0
                                    if (n - (n - x) // 2) > 0:
                                        # Check that n - (n - x) / 2 is even
                                        if (n - (n - x) // 2) % 2 == 0:
                                            # Check that (n - (n - x) / 2) / 2 is greater than 0
                                            if ((n - (n - x) // 2) // 2) > 0:
                                                # Check that (n - (n - x) / 2) / 2 is even
                                                if ((n - (n - x) // 2) // 2) % 2 == 0:
                                                    return True
        return False
    return False

