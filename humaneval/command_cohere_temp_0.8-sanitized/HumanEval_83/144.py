def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else: 
        # Split counts into those that start with 1 and those that end with 1.
        start_count = (n - 1) // 2
        end_start_count = (n - 1) // 2 + 1
        total = start_count + end_start_count
        return total