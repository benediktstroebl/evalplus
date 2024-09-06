
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # First get the range of numbers that we need to check
    min_number = 10**(n-1) + 1
    max_number = 10**n - 1
    
    # Now count how many numbers start with 1 and how many end with 1
    count_start = count_end = 0
    for number in range(min_number, max_number+1):
        if str(number).startswith('1'):
            count_start += 1
        if str(number).endswith('1'):
            count_end += 1
    return count_start + count_end
