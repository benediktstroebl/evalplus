def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a possible list of n-digit numbers from 1 to n*10^n
    num_list = list(range(n*10**n, 10//2, -1))

    # Filter out numbers that don't start or end with 1
    filtered_list = [num for num in num_list if (num//10 + num%10 == 1) or (num//10 - num%10 == 1)]

    # Return the length of filtered numbers list
    return len(filtered_list)