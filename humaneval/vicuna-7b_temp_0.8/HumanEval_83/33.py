
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Check for n=1, 2
    if n == 1 or n == 2:
        return 2
    # Check for n=3 case, since n=3 is the base case
    elif n == 3:
        return 2
    # For n>=4
    else:
        # Check n=4 case
        if n == 4:
            return 2
        # Check n-1 digit
        d = n-1
        # Count starts and ends
        c_starts = 0
        c_ends = 0
        # For each digit d
        for i in range(1, d+1):
            # For each digit i
            for j in range(1, d+1):
                # If the sum of i and j is <= d and i+j=n
                if j < d and i+j == n and (i+1) % d == 0 and (j+1) % d == 0:
                    c_starts += 1
            # If the sum of i and j is >= d and i+j=n
            if j < d and i+j == n and (i+1) % d == 0 and (j+1) % d == 0:
                c_ends += 1
        # Return the result
        return c_starts + c_ends
