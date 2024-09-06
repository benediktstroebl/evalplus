def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a string of n digits
    num = "".join(str(x) for x in range(1, n + 1))
    # Create the 2^n possible numbers from this template
    numbers = [num[i:] + str(num[:i]) for i in range(n)] + [num + '1']
    # Count the ones that start or end with 1
    return sum(1 for x in numbers if x[0] == '1' or x[-1] == '1')