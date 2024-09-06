
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Convert n to a string
    n = str(n)
    # List of all possible n-digit numbers
    nums = [int(n * i) for i in range(1, 10)]
    # Filter to all n-digit numbers that start or end with 1
    one_nums = [num for num in nums if str(num).startswith("1") or str(num).endswith("1")]
    # Return the length of that list
    return len(one_nums)
