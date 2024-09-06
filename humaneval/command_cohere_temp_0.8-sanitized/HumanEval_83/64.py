def starts_one_ends(n):
    assert n > 0, "n should be a positive integer"
    
    # Calculate the count of numbers that start with 1.
    start_with_1 = 1 if n == 1 else 99999999 / 10 ** (n - 1)
    
    # Calculate the count of numbers that end with 1.
    ends_with_1 = 1 if n == 1 else 10 ** (n - 1) / 99999999
    
    # Return the sum of counts.
    return start_with_1 + ends_with_1