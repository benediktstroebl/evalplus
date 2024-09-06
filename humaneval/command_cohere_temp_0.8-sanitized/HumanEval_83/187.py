def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Generate all n-digit numbers where the leading digit (start) cannot be 0, and the trailing digit (end) is optional
    numbers = [str(i) for i in range(1, 10)**n]
    
    # Count numbers that start or end with 1
    return sum(1 for num in numbers if num[0] == '1' or num[-1] == '1')